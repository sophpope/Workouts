import { View, Text, TextInput, Pressable } from 'react-native';
import { useState } from 'react';
import styles from '../styles/formStyles.js';

export default function CreateWorkout() {
    const [workoutName, setWorkoutName] = useState('');
    const [workoutDate, setWorkoutDate] = useState('');
    const [notes, setNotes] = useState('');

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

            <Pressable>
                <Text style={styles.workoutButton}>Create Workout</Text>
            </Pressable>
        </View>
    );
}