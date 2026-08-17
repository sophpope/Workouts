import React, { useEffect, useState} from 'react';
import AddUserForm from './AddUserForm';
import api from '../api.js';

function UserList( ){
    const [users, setUsers] = useState([])

    const fetchUsers = async () => {
        try{
            const response = await api.get('/users');
            setUsers(response.data.users);
        } catch (error) {
            console.error("Error fetching users", error);
        }
    };

    const addUser = async (username, email, password) =>{
        const response = api.post('/create_new_user', {
                username: username,
                email: email,
                password_hash: password
            });
            await fetchUsers();

            return (await response).data;
        
    };
    

    useEffect(() => {
        fetchUsers();
    }, []);

    return(
        <AddUserForm addUser={addUser} />
    )
 
};

export default UserList;