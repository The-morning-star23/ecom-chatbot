import React from 'react';

export default function ProductCard({ product }) {
  return (
    <div className="border rounded p-4 shadow-sm">
      <img src={product.image_url} alt={product.name} className="w-32 h-32 object-cover mb-2" />
      <h3 className="font-bold">{product.name}</h3>
      <p>{product.description}</p>
      <p>₹{product.price}</p>
      <p className="text-sm text-gray-500">{product.category}</p>
    </div>
  );
}
