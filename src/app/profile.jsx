import { useEffect, useState } from 'react';
import { View, Text, Pressable} from 'react-native';  
import api from '../api';
import AsyncStorage from '@react-native-async-storage/async-storage';   
import { useRouter, Link } from 'expo-router';
import WorkoutList from '../components/WorkoutList';
import styles from '../styles/formStyles';

export default function Profile() {
    const [user, setUser] = useState(null);
    const [workouts, setWorkouts] = useState([]);

    const fetchUserProfile = async () => {
        try {
            const token = await AsyncStorage.getItem('access_token');

            if (token){
                api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            }

            const response = await api.get('/me');
            setUser(response.data);

            const workoutResponse = await api.get('/get_workout');
            setWorkouts(workoutResponse.data);

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

        {user && (<Text style={styles.profile}>Welcome back {user.username}</Text>)}

        <Link href="/create-workout" style={styles.workoutButton} >
            Create New Workout
        </Link>

        <WorkoutList workouts={workouts} />

        <Pressable style={styles.buttonLink} onPress={handleLogout}>
            <Text>Logout</Text>
        </Pressable>
        </View>
    );
    }