import {Link} from "react-router-dom";
import React from "react";

const Navbar = () => {
    return (
        <nav className="bg-blue-500 p-4 text-white shadow-md">
            <div className="container mx-auto">
                <div className="flex justify-between">
                    <div className="font-bold text-xl">Seeker</div>
                    <ul className="space-x-4">
                        <li className="inline-block"><Link to="/">Login</Link></li>
                        <li className="inline-block"><Link to="/signup">Sign Up</Link></li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;