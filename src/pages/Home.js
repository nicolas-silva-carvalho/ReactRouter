import React from "react";
import "../pages/Home.css";
import { Link } from "react-router-dom";
import { useFetch } from "../hooks/useFetch";
const Home = () => {
  const url = "http://localhost:3000/products";
  const { data: items, loading } = useFetch(url);
  return (
    <div>
      <h1>Produtos</h1>
      <ul className="products">
        {items &&
          items.map((product) => (
            <li key={product.id}>
              <h2>{product.name}</h2>
              <p>{product.price}</p>
              <Link to={`/products/${product.id}`}>Detalhes</Link>
            </li>
          ))}
      </ul>
    </div>
  );
};

export default Home;
