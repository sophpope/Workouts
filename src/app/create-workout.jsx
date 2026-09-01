import { View, Text, TextInput, Pressable } from 'react-native';
import { useState } from 'react';
import styles from '../styles/formStyles.js';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useRouter } from 'expo-router';
import api from '../api.js';


export default function CreateWorkout() {
    const [workoutName, setWorkoutName] = useState('');
    const [workoutDate, setWorkoutDate] = useState('');
    const [notes, setNotes] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const router = useRouter();

    const handleCreateWorkout = async () => {
        if (!workoutName.trim()) {
            setError("Please enter a workout name");
            return;
        } else if (!workoutDate.trim()) {
            setError("Please enter a workout date");
            return;
        }

        setError('');

        try {
            const token = await AsyncStorage.getItem('access_token');
            if (token) {
                api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            }


            const response = await api.post('/create_workout', {
                workout_name: workoutName,
                workout_date: workoutDate,
                notes: notes
            });

            setSuccess(`Workout ${response.data.workout_name} created successfully`);

            setWorkoutName('');
            setWorkoutDate('');
            setNotes('');

            router.replace('/profile');

        } catch (error) {
            setError(error.response?.data?.detail || 'Error creating workout. Please check your details and try again.');
        }
    }
    return (
        <View>
            <Text style={styles.title}>Create Workout</Text>

            <TextInput
                style={styles.input}
                placeholder="Workout Name"
                placeholderTextColor='grey'
                value={workoutName}
                onChangeText={setWorkoutName}
            />

            <TextInput
                style={styles.input}
                placeholder="Workout Date YYYY-MM-DD"
                placeholderTextColor='grey'
                value={workoutDate}
                onChangeText={setWorkoutDate}
            />  

            <TextInput
                style={styles.input}
                placeholder="Notes"
                placeholderTextColor='grey'
                value={notes}
                onChangeText={setNotes}
            />

            {error && <Text style={styles.error}>{error}</Text>}

            {success && <Text style={styles.success}>{success}</Text>}

            <Pressable onPress={handleCreateWorkout}>
                <Text style={styles.workoutButton}>Create Workout</Text>
            </Pressable>
        </View>
    );
}