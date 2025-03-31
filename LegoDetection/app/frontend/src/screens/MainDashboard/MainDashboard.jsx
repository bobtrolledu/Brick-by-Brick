import React, { useState, useEffect } from "react";
import { BrickList } from "../../components/BrickList";
import { AddBrickForm } from "../../components/AddBrickForm";
import { VideoFeed } from "../../components/VideoFeed";
import { Button } from '../../components/ui/button';
import { Sun, Moon } from "lucide-react";
import io from "socket.io-client";

export const MainDashboard = () => {
  const [pieces, setPieces] = useState([]);
  const [theme, setTheme] = useState('light');
  const [isDetecting, setIsDetecting] = useState(true);
  
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    document.documentElement.classList.toggle('dark', savedTheme === 'dark');
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.classList.toggle('dark');
  };

  const fetchPieces = async () => {
    const response = await fetch('http://localhost:5000/api/get_pieces');
    const data = await response.json();
    setPieces(data);
  };

  useEffect(() => {
    fetchPieces();
    const socket = io("http://localhost:5000");
    
    socket.on('refresh-list', (data) => {
      setPieces(data.pieces);
    });

    return () => socket.disconnect();
  }, []);
  
  const handleAddPiece = async (formData) => {
    try {
      const response = await fetch('http://localhost:5000/api/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        fetchPieces();
      }
    } catch (error) {
      console.error('Error adding piece:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://localhost:5000/api/delete/${id}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        fetchPieces();
      }
    } catch (error) {
      console.error('Error deleting piece:', error);
    }
  };

  const handleDeleteAll = async () => {
    try {
      await fetch("http://localhost:5000/api/delete_all", {
        method: "POST",
      });
      fetchPieces();
    } catch (error) {
      console.error("Error clearing inventory:", error);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-end mb-4">
        <Button variant="outline" size="icon" onClick={toggleTheme}>
          {theme === 'light' ? (
            <Moon className="h-5 w-5" />
          ) : (
            <Sun className="h-5 w-5" />
          )}
        </Button>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="space-y-6">
          <div className="bg-card rounded-lg shadow-lg overflow-hidden">
            <VideoFeed isDetecting={isDetecting} setIsDetecting={setIsDetecting} />
          </div>
          <AddBrickForm onSubmit={handleAddPiece} />
        </div>
        <div className="bg-card rounded-lg shadow-lg p-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-bold">Inventory</h2>
            <button
              onClick={handleDeleteAll}
              className="text-destructive hover:text-destructive/90 text-sm font-medium"
            >
              Clear All
            </button>
          </div>
          <BrickList pieces={pieces} onDelete={handleDelete} />
        </div>
      </div>
    </div>
  );
};
