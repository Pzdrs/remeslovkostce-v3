import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL
});

export function getMediaURL(media: any) {
    return `${import.meta.env.VITE_BASE_DOMAIN}/media/${media}`;
}

export default api;
