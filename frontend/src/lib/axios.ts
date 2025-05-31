// lib/apiClient.ts
import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.NEXT_PUBLIC_BACKEND_BASE_URL || 'http://localhost:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Optionally allow CORS headers (though these are usually set by the server)
apiClient.defaults.headers.common = {
    ...apiClient.defaults.headers.common,
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PATCH',
    'Access-Control-Expose-Headers': '*',
};

// Add a response interceptor
apiClient.interceptors.response.use(
    (response) => {
        // Successful response
        return response;
    },
    (error) => {
        // Handle known errors
        if (error.response) {
            const status = error.response.status;

            // You can handle different status codes
            if (status === 401) {
                alert('Unauthorized, maybe redirect to login?');
            } else if (status === 403) {
                alert('Forbidden');
            } else if (status === 500) {
                alert('Server error');
            } else {
                console.error(`HTTP error: ${status}`, error.response.data);
            }
        } else if (error.request) {
            console.error('No response received from server:', error.request);
        } else {
            console.error('Error setting up request:', error.message);
        }

        // Optional: throw error again so components can also handle it
        return Promise.reject(error);
    }
);

export default apiClient;
