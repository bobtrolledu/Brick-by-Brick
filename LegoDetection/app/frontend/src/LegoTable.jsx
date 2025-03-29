import React, { useEffect, useState } from 'react';

const [legos, setLegos] = useState([]);

function LegoTable() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/get_bricks')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setLegos(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <table border="1" cellPadding="10" cellSpacing="0">
      <thead>
        <tr>
          <th>Name</th>
          <th>Color</th>
          <th>BrickID</th>
          <th>Quantity</th>
        </tr>
      </thead>
      <tbody>
        {legos.map((lego) => (
          <tr key={lego.id}>
            <td>{lego.name}</td>
            <td>{lego.color}</td>
            <td>{lego.brickid}</td>
            <td>{lego.quantity}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default LegoTable;