import React, { useEffect, useState } from 'react';
import ExerciseListItem from './ExerciseListItem';  
import api from '../api.js';    
import { FlatList } from 'react-native';

function ExerciseList() {
    const [exercises, setExercises] = useState([])

    const fetchExercises = async () => {
        try{
            const response = await api.get('/exercises');
            setExercises(response.data);
        } catch (error) {
            console.error("Error fetching exercises", error);
        }
    };

    const addExercise = async (exercise_name, primary_muscle, secondary_muscle, difficulty, category, equipment, description) => {
        const response = await api.post("/create_exercise", {
            exercise_name: exercise_name,
            primary_muscle: primary_muscle,
            secondary_muscle: secondary_muscle,
            difficulty: difficulty,
            category: category,
            equipment: equipment,
            description: description
            });
            await fetchExercises();

            return response.data;
        
    }
    useEffect(() => {
        fetchExercises();
    }, []);

    return(
        <FlatList
            data={exercises}
            contentContainerStyle={{gap:5}}
            keyExtractor={(item, index) => item.exercise_name + index}
            renderItem={({item}) => <ExerciseListItem item={item}/>}
        />
    );
}

export default ExerciseList;