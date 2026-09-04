import axios from 'axios';

const api = axios.create({
    baseURL: "http://localhost:8000"
});


// Checks is token is still valid, if not logs user out and redirects to login page
api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        if (error.response && error.response.status === 401) {
            await AsyncStorage.removeItem('access_token');
            delete api.defaults.headers.common['Authorization'];

            router.replace('/login');
        }
        return Promise.reject(error);
    }
);

export default api; 