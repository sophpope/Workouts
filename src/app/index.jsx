import { StatusBar } from 'expo-status-bar';
import { FlatList, StyleSheet, Text, View } from 'react-native';
import exercises from '../../assets/data/exercises.json';
import ExerciseListItem from '../components/ExerciseListItem';
import UserList from '../components/Users';
import { Link } from 'expo-router';
import styles from '../styles/formStyles';

export default function App() {

  return (
    <View style={styles.container}>

      <Link style={styles.Link} href="/login">
        Login
      </Link>

      <Link style={styles.Link} href="/register">
        Create Account
      </Link>

      <FlatList
        data={exercises}
        contentContainerStyle={{gap:5}}
        keyExtractor={(item, index) => item.name + index}
        renderItem={({item}) => <ExerciseListItem item={item}/>}
      />
      
      <StatusBar style="auto" />
    </View>
  );
}


