import React, {useState} from 'react';
import { View, Text, TextInput, Pressable } from 'react-native';
import api from '../api.js';
import styles from '../styles/formStyles.js';
import { Link, useRouter } from 'expo-router';
import AsyncStorage from '@react-native-async-storage/async-storage';


function LoginForm(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const router = useRouter();

    const handleLogin = async () => {
        setError('');
        setSuccess('');

        try{
            const response = await api.post('/login', {
                email: email,
                password: password
            });

            setSuccess(`Welcome ${response.data.username}! You have successfully logged in.`);

            const token = response.data.access_token;

            await AsyncStorage.setItem('access_token', token);

            api.defaults.headers.common['Authorization'] = `Bearer ${token}`;

            router.replace('/profile');

        } catch (error) {
            setError(error.response?.data?.detail || 'Error logging in. Please check your details and try again.');
        }
  
    };

    return (
        <View style={styles.form}>
            <Text style={styles.title}>Welcome Back</Text>
            <Text style={styles.subtitle}>Please enter your login details</Text>

            <TextInput 
                style={styles.input}
                value={email}
                onChangeText={setEmail}
                placeholder='Email'
                autoCapitalize='none'
                keyboardType='email-address'
            />

            <TextInput
                style={styles.input}
                value={password}
                onChangeText={setPassword}
                placeholder='Password'
                secureTextEntry
            />

            {error && <Text>{error}</Text>}
            {success && <Text>{success}</Text>}

            <Pressable 
                style={styles.button}
                onPress={handleLogin}>
                <Text style={styles.buttonText}>Login</Text>
            </Pressable>

            <Link href="/register" style={styles.linkText}>
                Create account
            </Link>
        </View>
    );

}

export default LoginForm;