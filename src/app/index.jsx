import { StatusBar } from 'expo-status-bar';
import { FlatList, Pressable, StyleSheet, Text, View } from 'react-native';
//import exercises from '../../assets/data/exercises.json';
import ExerciseList from '../components/Exercises';
import UserList from '../components/Users';
import { Link } from 'expo-router';
import styles from '../styles/formStyles';

export default function App() {

  return (
    <View style={styles.container}>

      <Link href="/login" asChild>
        <Pressable style={styles.buttonLink}>
          <Text style={styles.buttonText}>Login</Text>
        </Pressable>
      </Link>
      

      <Link href="/register" asChild>
        <Pressable style={styles.buttonLink}>
          <Text style={styles.buttonText}>Create Account</Text>
        </Pressable>
      </Link>

      {/* <FlatList
        data={exercises}
        contentContainerStyle={{gap:5}}
        keyExtractor={(item, index) => item.name + index}
        renderItem={({item}) => <ExerciseListItem item={item}/>}
      /> */}
      
      <ExerciseList />
      
      <StatusBar style="auto" />
    </View>
  );
}


