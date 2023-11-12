import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
    Navigate
} from "react-router-dom";
import SignUp from "./components/Signup";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import ClubSeeker from "./components/Clubseeker";
import Pickinterests from "./components/Pickinterests";
import {userAtom} from "./atoms";
import {useAtom} from 'jotai';
import UserSeeker from "./components/SimilarUsers";
import PickClubs from "./components/PickClubs";
const App = () => {
    const [user,] = useAtom(userAtom);
  return (
      <Router>
        <Navbar />
        <Routes>
            <Route path="/signup" element={user ? <Navigate to='/home' /> : <SignUp />}></Route>
            <Route path="/" element={user ? <Navigate to='/home' /> : <Login />}></Route>
            <Route path="/home" element={user ? <ClubSeeker /> : <Navigate to='/' />}></Route>
            <Route path="/updateProfile" element={user ? <Pickinterests /> : <Navigate to='/home' />}></Route>
            <Route path = "/findUsers" element={user ? <UserSeeker /> : <Navigate to='/home' />}></Route>
            <Route path = "/setClubs" element={user ? <PickClubs /> : <Navigate to='/home' />}></Route>
        </Routes>
      </Router>
  );
};
export default App;