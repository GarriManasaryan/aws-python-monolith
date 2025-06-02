'use client';

import { useEffect, useState } from 'react';
import { axiosConf } from '../axiosConf';
import { UserBackofficeModel } from '../client-models/users/UserBackofficeModel';

export default function UsersPage() {
    const [users, setUsers] = useState<UserBackofficeModel[]>([]);
    const [name, setName] = useState('');
    const [loading, setLoading] = useState(false);

    const fetchUsers = () => {
        axiosConf.get("/users").then((response) => {
            setUsers(response.data);
        })
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    const handleSubmit = async () => {
        if (!name.trim()) return;
        setLoading(true);
        try {
            axiosConf.post("/users", {name: name})
            .then(()=>{
                fetchUsers();
            })
            .then(()=>{
                setName('');
            })
            ;
        } catch (error) {
            console.error("Error creating user:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Users</h1>
            <ul>
                {users.map(u => (
                    <li key={u.id}>{u.name}</li>
                ))}
            </ul>

            <h2>Add New User</h2>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter user name"
                disabled={loading}
            />
            <button onClick={handleSubmit} disabled={loading || !name.trim()}>
                {loading ? "Adding..." : "Add User"}
            </button>
        </div>
    );
}
