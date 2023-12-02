import React, { useState} from 'react';
import {userAtom} from "../atoms";
import {useAtom} from 'jotai';
const UserSeeker = () => {
    const [interests, setInterests] = useState({ interest1: "", interest2: "", interest3: "" });
    const [users, setUsers] = useState([]);
    const [similarInterestUsers, setSimilarInterestUsers] = useState([]);
    const [user, ] = useAtom(userAtom);
    const [isFetched, setIsFetched] = useState(false);
    const [success, setSuccess] = useState(false);


    const fetchSimilarInterestUsers = async () => {
        setIsFetched(true);
        const currentUser = { email: user.email };

        try {
           
            const response = await fetch('http://localhost:5000/findSimilarUsers', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(currentUser)
            });

            if (response.ok) {
                const data = await response.json();
                setSimilarInterestUsers(data["user_list"]);
            } else {
                console.error("Error fetching users with similar interests:", response.statusText);
            }
        } catch (error) {
            console.error("Network error:", error);
        }
    };

    const handleDropdownChange = (e, interest) => {
        const newInterests = { ...interests };
        newInterests[interest] = e.target.value;
        setInterests(newInterests);
    };

    const searchUsers = async () => {
        setSuccess(true);
        const currentUser = { email: user.email };

        try {
            const response = await fetch('http://localhost:5000/findSimilarUsersWithInterests', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({interests, currentUser})
            });

            if (response.ok) {
                const data = await response.json();
                setUsers(data['user_list']);
            } else {
                console.error("Error fetching users:", response.statusText);
            }
        } catch (error) {
            console.error("Network error:", error);
        }
    };

    return (
        <div className="min-h-screen bg-violet-100 flex items-center justify-center p-4">
            <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md transition-transform transform hover:scale-102">
                <div className="mb-6">
                    <button onClick={fetchSimilarInterestUsers}
                            className="btn btn-primary w-full mt-6 text-white bg-blue-500 hover:bg-blue-600 rounded-lg py-2">
                        Find Users with Similar Interests
                    </button>
                </div>
                {isFetched &&
                    (<div className="mb-6">
                            <h2 className="text-2xl font-semibold text-gray-800 mb-4">Users with Similar Interests:</h2>
                            <ul>
                                {similarInterestUsers.length > 0
                                    ? (similarInterestUsers.map((user, index) => (
                                        <li key={index} className="p-2 bg-blue-100 rounded-lg transition-shadow hover:shadow-md text-blue-800 font-medium mb-4">{user}</li>
                                    ))) :((<div className="text-gray-600">No users found</div>))}
                            </ul>
                        </div>
                    )}

                <div className="space-y-6">
                    {['interest1', 'interest2', 'interest3'].map((interest, idx) => (
                        <div key={idx} className="relative">
                            <select onChange={(e) => handleDropdownChange(e, interest)}
                                    className="block appearance-none w-full bg-white border border-gray-300 hover:border-gray-400 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline-blue focus:border-blue-300">
                                <option value="">Select Interest</option>
                                <option value="Consulting">Consulting</option>
                                <option value="Computer Science">Computer Science</option>
                                <option value="Business">Business</option>
                                <option value="Robotics">Robotics</option>
                                <option value="Sports">Sports</option>
                                <option value="Martial Arts">Martial Arts</option>
                                <option value="Motorcycle">Motorcycle</option>
                                <option value="Gaming">Gaming</option>
                                <option value="Music">Music</option>
                                <option value="Engineering">Engineering</option>
                            </select>
                            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                                <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M5.293 9.293L10 14.586 14.707 9.293a.999.999 0 111.414 1.414l-5 5a.997.997 0 01-1.414 0l-5-5a.999.999 0 111.414-1.414z"/></svg>
                            </div>
                        </div>
                    ))}

                    <button onClick={searchUsers}
                            className="btn btn-primary w-full mt-6 text-white bg-blue-500 hover:bg-blue-600 rounded-lg py-2 transition-transform transform hover:scale-105">
                        Search
                    </button>
                </div>
                {success &&  (users.length > 0 ? (
                    <div className="mt-8 space-y-4">
                        <h2 className="text-2xl font-semibold text-gray-800 mb-4">Matching Users:</h2>
                        <ul>
                            {users.map((user, index) => (
                                <li key={index} className="p-2 bg-blue-100 rounded-lg transition-shadow hover:shadow-md text-blue-800 font-medium mb-4">{user}</li>
                            ))}
                        </ul>
                    </div>
                ) : (<div className="text-gray-600">No users found</div>))}
            </div>
        </div>
    );
};

export default UserSeeker;