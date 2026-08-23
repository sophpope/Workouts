import { useEffect, useState } from 'react';
import { View, Text, Pressable } from 'react-native';  
import api from '../api';
import AsyncStorage from '@react-native-async-storage/async-storage';   
import { useRouter } from 'expo-router';

export default function Profile() {
    const [user, setUser] = useState(null);

    const fetchUserProfile = async () => {
        try {
            const token = await AsyncStorage.getItem('access_token');

            if (token){
                api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            }

            const response = await api.get('/me');
            setUser(response.data);

        } catch (error) {
            console.error('Error fetching user profile:', error);
        }
    };

    /* setting up logout */
    const router = useRouter();

    const handleLogout = async () => {
        try {
            await AsyncStorage.removeItem('access_token');

            delete api.defaults.headers.common['Authorization'];

            router.replace('/login');

        } catch (error) {
            console.error('Error logging out:', error);
        }
    };

    useEffect(() => {
        fetchUserProfile();
    }, []);

    return (
        <View>
        <Text>Profile</Text>

        {user && (<Text>Welcome back {user.username}</Text>)}

        <Pressable onPress={handleLogout}>
            <Text>Logout</Text>
        </Pressable>
        </View>
    );
    }