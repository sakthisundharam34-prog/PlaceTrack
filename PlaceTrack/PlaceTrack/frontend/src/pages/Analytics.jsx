import React, { useEffect, useState } from 'react';
import { api } from '../services/api';

function Analytics() {
  const [deptStats, setDeptStats] = useState([]);

  useEffect(() => {
    api.get('/analytics/department-stats/')
       .then(res => setDeptStats(res.data))
       .catch(err => console.error(err));
  }, []);

  return (
    <section>
      <h2>Analytics & Reports</h2>
      <p className="subtitle">Visual breakdowns of placement performance across various parameters.</p>
      
      <div className="card" style={{ maxWidth: '800px' }}>
        <h3>Department-wise Placement</h3>
        
        {deptStats.length === 0 ? (
          <p className="empty">Loading analytics...</p>
        ) : (
          deptStats.map(stat => (
            <div className="bar" key={stat.department}>
              <span>{stat.department}</span>
              <div>
                <i style={{ width: `${stat.percentage}%` }}></i>
              </div>
              <b>{stat.percentage}%</b>
            </div>
          ))
        )}
      </div>
    </section>
  );
}

export default Analytics;
