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
        padding: 10, 
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
        marginBottom: 10,
        color: 'black',
        marginTop: 10, 
        marginLeft: 10,
        marginRight: 10,
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

    Link: {
        fontSize: 18,
        color: '#1E90FF',
        marginBottom: 10,

    },

    buttonLink:{
        backgroundColor: '#1E90FF',
        padding: 10,
        borderRadius: 8,
        alignItems: 'center',
        margin: 10,
    },

    container: {
        flex: 1,
        backgroundColor: '#BFDCD8',
        justifyContent: 'center',
        padding:10,

    },

    exerciseContainer: {
        padding:10,
        gap: 10,
    },
        
    panel: {
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
    },
    exerciseName: {
        fontSize:24, 
        fontWeight: '500',
    },
    exerciseSubtitle: {
        color: 'dimgray'
    },
    subValue:{
        textTransform: 'capitalize'
    },
    instructions:{
        fontSize: 16,
        lineHeight: 25,
    },
    seeMore:{
        alignSelf: 'center',
        padding: 5,
        fontWeight: '600',
        color: 'gray',
    }, 

    workoutName:{
        fontSize: 18,
        fontWeight: 'bold',
    },

    workoutText:{
        fontSize: 14,
        color: 'dimgray',
    },

    workoutContainer:{
        backgroundColor: 'white',
        padding: 10,
        borderRadius: 10,
        gap: 5,
        marginHorizontal: 2,
        marginLeft: 10,
        marginRight: 10,
    },

    profile:{
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
        marginTop: 10,
        marginLeft: 10,
    },

    workoutButton:{
        backgroundColor: '#90E6FC',
        padding: 10,
        borderRadius: 8,
        alignItems: 'center',
        margin: 10,
        color: 'white',
        textAlign: 'center',
    }


});
    export default styles;
   