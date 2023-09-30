import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import SignUp from "./components/Signup";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
const App = () => {
  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/signup" element={<SignUp />}></Route>
          <Route path="/" element={<Login />}></Route>
        </Routes>
      </Router>
  );
};
export default App;