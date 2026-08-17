import React, {useState} from 'react';
import {View, Text, TextInput, Pressable, StyleSheet} from 'react-native';

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
            setError(error.response?.data?.detail || 'Error creating user');
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

const styles = StyleSheet.create({

  form: {
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 16,
    marginBottom: 20,

  },

  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },

  subtitle: {
    fontSize: 16,
    marginBottom: 20,
  },

  label: {
    fontSize: 14,
    marginBottom: 5,
  },

  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    padding: 10,
    marginBottom: 15,
    color: 'black',
  },

  button: {
    backgroundColor: '#4CAF50',
    padding: 10,
    borderRadius: 8,
    alignItems: 'center',
  },

  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },  
  
  error: {
    color: 'red',
    marginBottom: 10,
  },

  success: {
    color: 'green',
    marginBottom: 10,
  },

})
export default AddUserForm;