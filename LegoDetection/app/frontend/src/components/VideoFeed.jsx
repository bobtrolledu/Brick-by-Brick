import React, { useEffect, useState } from "react";
import { Play, Pause, ToyBrick } from "lucide-react";
import { Button } from "./ui/button";
import io from "socket.io-client";

export const VideoFeed = ({ isDetecting, setIsDetecting }) => {
  const [brickInfo, setBrickInfo] = useState({
    id: "N/A",
    name: "N/A",
    confidence: 0,
    color: "N/A",
  });

  useEffect(() => {
    const socket = io("http://localhost:5000");

    fetch("http://localhost:5000/api/detection_status")
      .then((res) => res.json())
      .then((data) => setIsDetecting(data.detecting));

    socket.on("update_info", (data) => {
      if (isDetecting) {
        setBrickInfo(data);
      }
    });

    return () => socket.disconnect();
  }, [isDetecting]);

  const toggleDetection = async () => {
    try {
      const response = await fetch(
        "http://localhost:5000/api/toggle_detection",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ detecting: !isDetecting }),
        }
      );
      if (response.ok) {
        setIsDetecting(!isDetecting);
      }
    } catch (error) {
      console.error("Error toggling detection:", error);
    }
  };

  return (
    <div className="flex flex-col items-center">
      <div className="relative w-full max-w-screen-4xl">
        {/* Set video to display in 4K */}
        <img
          src="http://localhost:5000/video"
          alt="4K Video Feed"
          className="w-full h-auto shadow-lg"
          style={{ maxWidth: "3840px", maxHeight: "2160px" }}
        />
      </div>

      <div className="grid grid-cols-3 gap-x-6 m-6 w-full px-6">
        <div className="bg-card dark:bg-background p-4 rounded-lg shadow-lg flex flex-col items-center justify-center space-y-4">
          <Button
            onClick={toggleDetection}
            variant="outline"
            size="icon"
            className="h-12 w-12"
          >
            {isDetecting ? <Pause className="h-6 w-6" /> : <Play className="h-6 w-6" />}
          </Button>
          <div className="text-center space-y-2">
            <div className="flex items-center justify-center gap-2">
              <div className={`w-3 h-3 rounded-full ${isDetecting ? "bg-green-500" : "bg-red-500"}`}></div>
              <p className="text-sm text-muted-foreground">Detection {isDetecting ? "Active" : "Paused"}</p>
            </div>
          </div>
        </div>

        <div className="bg-card dark:bg-background p-4 rounded-lg shadow-lg flex flex-col items-center justify-center">
          <ToyBrick className="h-8 w-8 mb-2" />
          <div className="text-center">
            <p className="text-sm font-medium">{isDetecting ? brickInfo.name : "N/A"}</p>
            <p className="text-xs text-muted-foreground">ID: {isDetecting ? brickInfo.id : "N/A"}</p>
            <p className="text-xs text-muted-foreground">Color: {isDetecting ? brickInfo.color : "N/A"}</p>
          </div>
        </div>

        <div className="bg-card dark:bg-background p-4 rounded-lg shadow-lg flex flex-col items-center justify-center">
          <div className="text-2xl font-bold">{isDetecting ? brickInfo.confidence : "-1"}%</div>
          <p className="text-sm text-muted-foreground">Confidence</p>
        </div>
      </div>
    </div>
  );
};