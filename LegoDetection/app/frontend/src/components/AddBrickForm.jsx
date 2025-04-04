
import React, { useState } from 'react';
import { PlusCircle } from "lucide-react";
import { Button } from './ui/button';

export const AddBrickForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    name: '',
    color: '',
    brickid: '',
    quantity: 1
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({ name: '', color: '', brickid: '', quantity: 1 });
  };

  return (
    <form onSubmit={handleSubmit} className="flex items-center gap-2">
      <PlusCircle className="h-5 w-5 text-primary shrink-0" />
      <input
        type="text"
        placeholder="Name"
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        className="flex-1 px-2 py-1 rounded-md border bg-background text-sm min-w-0"
        required
      />
      <input
        type="text"
        placeholder="Color"
        value={formData.color}
        onChange={(e) => setFormData({ ...formData, color: e.target.value })}
        className="flex-1 px-2 py-1 rounded-md border bg-background text-sm min-w-0"
        required
      />
      <input
        type="text"
        placeholder="ID"
        value={formData.brickid}
        onChange={(e) => setFormData({ ...formData, brickid: e.target.value })}
        className="flex-1 px-2 py-1 rounded-md border bg-background text-sm min-w-0"
        required
      />
      <input
        type="number"
        placeholder="Qty"
        value={formData.quantity}
        onChange={(e) => setFormData({ ...formData, quantity: parseInt(e.target.value) })}
        className="w-16 px-2 py-1 rounded-md border bg-background text-sm"
        required
        min="1"
      />
      <Button type="submit" size="sm" className="shrink-0">Add</Button>
    </form>
  );
};
