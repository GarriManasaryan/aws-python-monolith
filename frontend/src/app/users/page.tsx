'use client';

import { useEffect, useState } from 'react';
import {UserBackofficeModel} from "@/client-models/users/UserBackofficeModel";
import apiClient from "@/lib/axios";

export default function UsersPage() {
    const [users, setUsers] = useState<UserBackofficeModel[]>([]);
    const [name, setName] = useState('');
    const [loading, setLoading] = useState(false);

    const fetchUsers = () => {
        apiClient.get("/users").then((response) => {
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
            apiClient.post("/users", {name: name});
            setName('');
            fetchUsers(); // refresh list after adding
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
