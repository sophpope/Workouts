import {View, Text, StyleSheet, ScrollView} from 'react-native';
import {useLocalSearchParams} from 'expo-router';
//import exercises from '../../assets/data/exercises.json'
import api from '../api';
import { useEffect } from 'react';
import {Stack} from 'expo-router'
import { useState } from 'react'
import styles from '../styles/formStyles';

export default function ExerciseDetailsScreen() {
    const params = useLocalSearchParams();

    const [isInstructionExpanded, setIsInstructionExpanded] = useState(false);

    const [exercise, setExercise] = useState(null);

    useEffect(() => {
        const fetchExercise = async () => {
            try {
                const response = await api.get(`/exercises/${params.id}`);
                setExercise(response.data);
            } catch (error) {
                console.error("Error fetching exercise", error);
            }
        };

        fetchExercise();
    }, [params.id]);


    if (!exercise) {
        return 
            <Text>
                Exercise not found
            </Text>;
    }

    return(
        <ScrollView contentContainerStyle={styles.exerciseContainer}>
            <Stack.Screen options={{title: exercise.exercise_name}} />

            <View style={styles.panel}>
                <Text style={styles.exerciseName}>{exercise.exercise_name}</Text>

                <Text style={styles.exerciseSubtitle}>
                    <Text style={styles.subValue}>{exercise.primary_muscle}</Text> |{' '}
                    <Text style={styles.subValue}>{exercise.equipment}</Text>
                </Text>
            </View>

            <View style={styles.panel}>
                <Text style={styles.instructions} numberOfLines={isInstructionExpanded ? 0:3}>{exercise.description}</Text>
                <Text style={styles.instructions}>Difficulty: {exercise.difficulty}</Text>
                <Text style={styles.instructions}>Category: {exercise.category}</Text>
                <Text style={styles.instructions}>Equipment: {exercise.equipment}</Text>
                <Text style={styles.instructions}>Primary Muscle: {exercise.primary_muscle}</Text>  
                <Text style={styles.instructions}>Secondary Muscle: {exercise.secondary_muscle}</Text>
                {/* <Text 
                onPress={() => setIsInstructionExpanded(!isInstructionExpanded)} 
                style={styles.seeMore}>
                    {isInstructionExpanded ? 'See Less' : 'See More ...'}
                    </Text> */}
            </View>
        </ScrollView>
    );
}
