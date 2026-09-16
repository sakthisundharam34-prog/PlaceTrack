import {createContext,useContext,useState} from 'react';
import {login} from '../services/api';
const C=createContext();
export function AuthProvider({children}){const [user,setUser]=useState(JSON.parse(localStorage.getItem('user')||'null')); const signIn=async(u,p)=>{const r=await login(u,p);localStorage.setItem('token',r.data.token);localStorage.setItem('user',JSON.stringify(r.data));setUser(r.data)}; const signOut=()=>{localStorage.clear();setUser(null)}; return <C.Provider value={{user,signIn,signOut}}>{children}</C.Provider>}; export const useAuth=()=>useContext(C);
