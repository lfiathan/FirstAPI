
// axios.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8080/api', // Ensure this matches your Nginx configuration
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;

