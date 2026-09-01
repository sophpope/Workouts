import { FlatList, Text, View } from "react-native";
import styles from "../styles/formStyles";



export default function WorkoutList({ workouts }) {
    return(
        <FlatList
            data={workouts}
            keyExtractor={(item) => item.id}
            renderItem={({ item }) => (
                <View style={styles.workoutContainer}>
                    <Text style={styles.workoutName}>{item.workout_name}</Text>
                    <Text style={styles.workoutText}>{item.workout_date}</Text>
                    <Text style={styles.workoutText}>{item.notes}</Text>
                </View>
            )}
        />  
    );
}