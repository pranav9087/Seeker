import {Link} from "react-router-dom";
import React from "react";
import {userAtom} from "../atoms";
import {useAtom} from 'jotai'

const Navbar = () => {
    const [user, setUser] = useAtom(userAtom);
    function handleClick() {
        setUser(null);
    }
    return (
        <nav className="bg-blue-500 p-4 text-white shadow-md">
            <div className="container mx-auto">
                <div className="flex justify-between">
                    <div className="font-bold text-xl">Seeker</div>
                    <ul className="space-x-4">
                        {!user && <li className="inline-block"><Link to="/">Login</Link></li>}
                        {!user && <li className="inline-block"><Link to="/signup">Sign Up</Link></li>}
                        {user && <li className="inline-block"><Link to="/home">Home</Link></li>}
                        {user && <li className="inline-block"><Link to="/updateProfile">Pick Interests</Link></li>}
                        {user && <li className="inline-block"><Link to="/setClubs">Pick Clubs</Link></li>}
                        {user && <li className="inline-block"><Link to="/findUsers">Find Users</Link></li>}
                        {user && <li className="inline-block" onClick={handleClick}><Link to="/">Logout</Link></li>}
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;