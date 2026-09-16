import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Layout({ children }) {
  const { user, signOut } = useAuth();
  
  return (
    <div className="app">
      <aside>
        <h1>🎓 PlaceTrack</h1>
        <p>Connect Students.<br/>Careers. Companies.</p>
        <nav>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/students">Students</Link>
          <Link to="/companies">Companies</Link>
          <Link to="/drives">Placement Drives</Link>
          <Link to="/applications">Applications</Link>
          <Link to="/placements">Placements</Link>
          <Link to="/analytics">Analytics</Link>
        </nav>
        <button onClick={signOut}>Logout</button>
      </aside>
      <main>
        <header>
          <h2>Welcome back, <b>{user?.username}</b></h2>
        </header>
        {children}
      </main>
    </div>
  );
}

export default Layout;
