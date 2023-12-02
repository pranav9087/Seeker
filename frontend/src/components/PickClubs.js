import React, { useState } from 'react';
import {userAtom} from "../atoms";
import {useAtom} from 'jotai';
const PickClubs = () => {
    const [interests, setInterests] = useState({ club1: "", club2: "", club3: "" });
    const [user, ] = useAtom(userAtom);
    const [success, setSuccess] = useState(false);
    const handleDropdownChange = (e, index) => {
        const newInterests = { ...interests };
        newInterests[index] = e.target.value;
        setInterests(newInterests);
    }

    const searchClubs = async () => {
        try {
            const response = await fetch('http://localhost:5000/updateClubs', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({email: user.email, clubs: interests})
            });

            if (response.ok) {
                setSuccess(true);
            } else {
                console.error("Error fetching clubs:", response.statusText);
            }
        } catch (error) {
            console.error("Network error:", error);
        }
    }

    return (
        <div className="min-h-screen bg-violet-100 flex items-center justify-center p-4">
            <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md transition-transform transform hover:scale-102">
                <h1 className="text-3xl font-bold mb-6 text-gray-800 text-center">Pick Clubs</h1>

                <div className="space-y-6">
                    {['club1', 'club2', 'club3'].map((interest, idx) => (
                        <div key={idx} className="relative">
                            <select onChange={(e) => handleDropdownChange(e, interest)}
                                    className="block appearance-none w-full bg-white border border-gray-300 hover:border-gray-400 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline-blue focus:border-blue-300">
                                <option value="">Select Clubs</option>
                                <option value="Illinois Business Consulting">Illinois Business Consulting</option>
                                <option value="Illinois Consulting Group">Illinois Consulting Group</option>
                                <option value="Students Consulting for Non-Profit Organizations">Students Consulting for Non-Profit Organizations</option>
                                <option value="Champaign-Urbana Business and Engineering Consulting">Champaign-Urbana Business and Engineering Consulting</option>
                                <option value="Founders">Founders</option>
                                <option value="ACM">ACM</option>
                                <option value="ZeroToOne">ZeroToOne</option>
                                <option value="D-Lab">D-Lab</option>
                                <option value="Illini Solar Car">Illini Solar Car</option>
                                <option value="Illinois Business Council">Illinois Business Council</option>
                                <option value="IlliniEV">IlliniEV</option>
                                <option value="Alpha Kappa Psi">Alpha Kappa Psi</option>
                                <option value="Phi Gamma Nu">Phi Gamma Nu</option>
                                <option value="Delta Sigma Pi">Delta Sigma Pi</option>
                                <option value="OTCR">OTCR</option>
                                <option value="Badminton For Fun">Badminton For Fun</option>
                                <option value="Illini Wushu">Illini Wushu</option>
                                <option value="Illini Motorcycle Club">Illini Motorcycle Club</option>
                                <option value="Social Gaming Club">Social Gaming Club</option>
                                <option value="Hip-Hop Collective">Hip-Hop Collective</option>
                                <option value="Engineering Council">Engineering Council</option>
                            </select>
                            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                                <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M5.293 9.293L10 14.586 14.707 9.293a.999.999 0 111.414 1.414l-5 5a.997.997 0 01-1.414 0l-5-5a.999.999 0 111.414-1.414z"/></svg>
                            </div>
                        </div>
                    ))}

                    <button onClick={searchClubs}
                            className="btn btn-primary w-full mt-6 text-white bg-blue-500 hover:bg-blue-600 rounded-lg py-2 transition-transform transform hover:scale-105">
                        Update Profile
                    </button>

                    {success && <p className="text-green-500">Successfully updated profile!</p>}
                </div>
            </div>
        </div>
    )
}

export default PickClubs;