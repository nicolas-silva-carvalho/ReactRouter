import "./App.css";
import { Route, BrowserRouter, Routes, Navigate } from "react-router-dom";

import NavBar from "./components/NavBar";
import SearchForm from "./components/SearchForm";

import Home from "./pages/Home";
import About from "./pages/About";
import Product from "./pages/Product";
import Info from "./pages/Info";
import NotFound from "./pages/NotFound";
import Search from "./pages/Search";

function App() {
  return (
    <div className="App">
      <h1>React Router</h1>
      <BrowserRouter>
        <NavBar></NavBar>
        <SearchForm></SearchForm>
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/about" element={<About></About>}></Route>
          <Route
            path="/company"
            element={<Navigate to={"/about"}></Navigate>}
          ></Route>
          <Route path="/products/:id/info" element={<Info></Info>}></Route>
          <Route path="/products/:id" element={<Product></Product>}></Route>
          <Route path="search" element={<Search></Search>}></Route>
          <Route path="*" element={<NotFound></NotFound>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
