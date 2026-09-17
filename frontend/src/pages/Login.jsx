import React, { useState } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Login() {
  const { user, signIn } = useAuth();
  const nav = useNavigate();
  const [username, setUsername] = useState('sakthi');
  const [password, setPassword] = useState('sakthi123');
  const [error, setError] = useState('');

  if (user) return <Navigate to="/dashboard" />;

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await signIn(username, password);
      nav('/dashboard');
    } catch (x) {
      setError('Invalid credentials. Please check your username and password.');
    }
  };

  return (
    <div className="auth">
      <div className="card">
        <h1>🎓 PlaceTrack</h1>
        <p>Placement Management System</p>
        
        <form onSubmit={handleLogin}>
          <input 
            type="text" 
            placeholder="Username" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
          />
          <input 
            type="password" 
            placeholder="Password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
          />
          <button type="submit">Log In</button>
        </form>
        
        {error && <span className="error">{error}</span>}
        <br/>
        <small>Use the default credentials to login.</small>
      </div>
    </div>
  );
}

export default Login;
