import React from "react";

const Login = () => {
    return (
        <div className="min-h-screen flex items-center justify-center bg-violet-100">
            <div className="bg-gradient-to-br from-purple-200 via-pink-200 to-red-200 p-8 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-bold mb-4 text-gray-700">Login</h2>
                <input type="email" className="input input-bordered w-full mb-2 bg-white bg-opacity-80" placeholder="Email" />
                <input type="password" className="input input-bordered w-full mb-2 bg-white bg-opacity-80" placeholder="Password" />
                <button className="btn btn-purple w-full mt-3">Login</button>
            </div>
        </div>
    );
};

export default Login;