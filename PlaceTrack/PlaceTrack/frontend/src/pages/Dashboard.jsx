import React, { useEffect, useState } from 'react';
import { api } from '../services/api';

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get('/analytics/overview/')
       .then(res => setStats(res.data))
       .catch(err => console.error(err));
  }, []);

  const formatValue = (key, value) => {
    if (value == null) return '—';
    if (key.includes('package')) return `₹${Number(value).toFixed(2)} LPA`;
    if (key.includes('percentage')) return `${Number(value).toFixed(2)}%`;
    return value;
  };

  const statConfig = [
    { label: 'Total Students', key: 'total_students' },
    { label: 'Total Companies', key: 'total_companies' },
    { label: 'Active Drives', key: 'active_drives' },
    { label: 'Students Placed', key: 'students_placed' },
    { label: 'Placement Rate', key: 'placement_percentage' },
    { label: 'Avg Package', key: 'average_package' }
  ];

  return (
    <section>
      <h2>Dashboard</h2>
      <p className="subtitle">High-level overview of the college placement system.</p>
      
      <div className="stats">
        {statConfig.map((item) => (
          <div className="stat" key={item.key}>
            <span>{item.label}</span>
            <strong>{stats ? formatValue(item.key, stats[item.key]) : 'Loading...'}</strong>
          </div>
        ))}
      </div>
      
      <div className="card">
        <h3>Live Data Connection</h3>
        <p>All numbers on this dashboard are dynamically calculated in real-time from the SQLite database via Django REST Framework APIs. As you add students or update applications, these numbers will automatically reflect the latest state.</p>
      </div>
    </section>
  );
}

export default Dashboard;
