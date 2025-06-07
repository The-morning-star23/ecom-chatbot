import React, { useState } from 'react';
import api from '../api';

export default function Login({ setLoggedIn }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      await api.post('/auth/login', { username, password });
      setLoggedIn(true);
    } catch (err) {
      alert('Login failed');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl mb-2">Login</h2>
      <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} className="border p-2 mr-2" />
      <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} className="border p-2 mr-2" />
      <button onClick={handleLogin} className="bg-blue-500 text-white px-4 py-2">Login</button>
    </div>
  );
}
