import React, {useState} from 'react';
import {View, Text, TextInput, Pressable} from 'react-native';
import styles from '../styles/formStyles.js';

const placeholderColour = 'grey';

function AddUserForm({ addUser }) {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleSubmit = async () => {
        
        if (!username.trim()){
            setError("Please enter a username")
            return;
        }else if(!email.trim()){
            setError("Please enter an email address")
            return;
        }else if(!password.trim()){
            setError("Please enter a password")
            return;
        }

        setError('');

        try{
            const createdUser = await addUser(username, email, password);

            setUsername('');
            setEmail('');
            setPassword('');

            setSuccess(`User ${createdUser.username} created successfully`);
        } catch (error){
            const detail = error.response?.data?.detail;

            if (typeof detail === 'string') {
                setError(detail);
            } else if (Array.isArray(detail) && detail.length > 0) {
              const emailError = detail.find((item) => item.loc?.includes('email'));

              if (emailError) {
                    setError('Please enter a valid email address');
                } else {
                    setError('Please check your details and try again');
                }
            
            } else {
              setError('Error creating user');
            }
          }
    };

    return (
        <View style={styles.form}>
          <Text style={styles.title}>Please create your user</Text>
          <Text style={styles.subtitle}>Enter your user details</Text>

          
          <TextInput
            style={styles.input}
            value={username}
            onChangeText={setUsername}
            placeholder="Enter your username"
            placeholderTextColor={placeholderColour}
            autoCapitalize="none"
          />
      
          <TextInput
            style={styles.input}
            value={email}
            onChangeText={setEmail}
            placeholder="Enter your email address"
            placeholderTextColor={placeholderColour}
            keyboardType="email-address"
            autoCapitalize="none"
          />
      
          <TextInput
            style={styles.input}
            value={password}
            onChangeText={setPassword}
            placeholder="Enter your password"
            placeholderTextColor={placeholderColour}
            secureTextEntry
          />

          {error ? (
            <Text style={styles.error}>{error}</Text>
          ) :null }

          {success ? (
            <Text style={styles.success}>{success}</Text>
          ) : null}
      
          <Pressable style={styles.button} onPress={handleSubmit}>
            <Text style={styles.buttonText}>Create Account</Text>
          </Pressable>
        </View>
      );
    }

export default AddUserForm;