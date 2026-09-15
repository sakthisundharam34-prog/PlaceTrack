import axios from 'axios';
export const api=axios.create({baseURL:'http://127.0.0.1:8000/api'});
api.interceptors.request.use(c=>{const t=localStorage.getItem('token'); if(t)c.headers.Authorization=`Token ${t}`; return c});
export const login=(username,password)=>api.post('/auth/login/',{username,password});
