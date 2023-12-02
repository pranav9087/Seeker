import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {userAtom} from "../atoms";
import {useAtom} from 'jotai'

const SignUp = () => {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [failure, setFailure] = useState(false);

    const navigate = useNavigate();
    const [, setUser] = useAtom(userAtom);
    const handleSubmitClick = async () => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                'username': name,
                'email_address': email,
                'password': password
            })
        };
        try {
            const response = await fetch('http://localhost:5000/register', requestOptions);
            if (response.ok) {
                const data = response.json();
                setUser(data);
                localStorage.setItem('user', JSON.stringify(data));
                navigate('/home');
            } else {
                setFailure(true);
                console.error("There was an error during the sign-up:");
            }
        } catch (error) {
            setFailure(true);
            console.error("There was an error during the sign-up:", error);
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-violet-100">
            <div className="bg-gradient-to-br from-purple-200 via-pink-200 to-red-200 p-8 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-bold mb-4 text-gray-700">Sign Up</h2>
                <input type="text" className="input input-bordered w-full mb-2 bg-white bg-opacity-80" placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
                <input type="email" className="input input-bordered w-full mb-2 bg-white bg-opacity-80" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
                <input type="password" className="input input-bordered w-full mb-2 bg-white bg-opacity-80" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                <button className="btn btn-purple w-full mt-3" onClick={handleSubmitClick}>Sign Up</button>
                {failure && <p className="text-red-500 text-sm mt-2">Error while registering.</p>}
            </div>
        </div>
    );
};

export default SignUp;
