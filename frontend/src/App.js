import React, { useState } from 'react';
import Chatbot from './components/Chatbot';
import Login from './components/Login';

export default function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div className="max-w-4xl mx-auto mt-6">
      {loggedIn ? <Chatbot /> : <Login setLoggedIn={setLoggedIn} />}
    </div>
  );
}
