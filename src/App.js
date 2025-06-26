import "./App.css";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import NavBar from "./components/NavBar";

function App() {
  return (
    <div className="App">
      <h1>React Router</h1>
      <BrowserRouter>
        <NavBar></NavBar>
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/about" element={<About></About>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
