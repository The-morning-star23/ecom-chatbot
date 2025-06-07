import React, { useState } from 'react';
import api from '../api';
import ProductCard from './ProductCard';

export default function Chatbot() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const res = await api.get('/products/search', { params: { q: query } });
    setResults(res.data);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl mb-2">Ask for a product</h2>
      <input type="text" value={query} onChange={e => setQuery(e.target.value)} className="border p-2 mr-2" />
      <button onClick={handleSearch} className="bg-green-600 text-white px-4 py-2">Search</button>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
        {results.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  );
}
