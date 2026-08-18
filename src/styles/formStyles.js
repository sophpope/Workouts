import { StyleSheet } from 'react-native';    

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

    export default styles;