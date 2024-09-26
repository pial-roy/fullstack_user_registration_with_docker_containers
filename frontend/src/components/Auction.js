import React, { useEffect, useState } from 'react';

function Auction() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/')  // Change to the appropriate API endpoint
      .then(response => response.json())
      .then(data => setMessage(data.message));
  }, []);

  return <h2>{message}</h2>;
}

export default Auction;