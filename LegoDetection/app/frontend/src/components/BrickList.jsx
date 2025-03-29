
import React from 'react';
import { Trash2Icon } from "lucide-react";

export const BrickList = ({ pieces, onDelete }) => {
  return (
    <div className="overflow-x-auto border rounded-lg">
      <div className="max-h-[600px] overflow-y-auto">
        <table className="w-full divide-y divide-border">
          <thead className="bg-muted sticky top-0">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-bold text-muted-foreground uppercase tracking-wider">Name</th>
              <th className="px-6 py-3 text-left text-xs font-bold text-muted-foreground uppercase tracking-wider">Color</th>
              <th className="px-6 py-3 text-left text-xs font-bold text-muted-foreground uppercase tracking-wider">Brick ID</th>
              <th className="px-6 py-3 text-left text-xs font-bold text-muted-foreground uppercase tracking-wider">Quantity</th>
              <th className="px-6 py-3 text-left text-xs font-bold text-muted-foreground uppercase tracking-wider"> </th>
            </tr>
          </thead>
          <tbody className="bg-card divide-y divide-border">
            {pieces.map((piece) => (
              <tr key={piece.id} className="hover:bg-muted/50">
                <td className="px-6 py-4 text-sm max-w-[200px] truncate">{piece.name}</td>
                <td className="px-6 py-4 text-sm max-w-[100px] truncate">{piece.color}</td>
                <td className="px-6 py-4 text-sm max-w-[150px] truncate">{piece.brickid}</td>
                <td className="px-6 py-4 text-sm">{piece.quantity}</td>
                <td className="px-6 py-4 whitespace-nowrap text-sm">
                  <button
                    onClick={() => onDelete(piece.id)}
                    className="text-destructive hover:text-destructive/90"
                  >
                    <Trash2Icon className="h-5 w-5" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
