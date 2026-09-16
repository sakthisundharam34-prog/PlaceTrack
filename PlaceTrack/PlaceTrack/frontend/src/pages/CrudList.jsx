import React, { useEffect, useState } from 'react';
import { api } from '../services/api';

const resources = {
  students: {
    title: 'Students',
    path: '/students/',
    fields: ['student_id', 'name', 'email', 'department', 'year', 'cgpa', 'skills', 'backlogs', 'placement_status']
  },
  companies: {
    title: 'Companies',
    path: '/companies/',
    fields: ['company_name', 'industry', 'location', 'email', 'website']
  },
  drives: {
    title: 'Placement Drives',
    path: '/drives/',
    fields: ['company', 'job_role', 'package', 'eligibility_cgpa', 'drive_date', 'application_deadline', 'status']
  },
  applications: {
    title: 'Applications',
    path: '/applications/',
    fields: ['student', 'placement_drive', 'status']
  },
  placements: {
    title: 'Placements',
    path: '/placements/',
    fields: ['student', 'company', 'placement_drive', 'job_role', 'package', 'placement_date', 'joining_date', 'status']
  }
};

function CrudList({ type }) {
  const resource = resources[type];
  const [data, setData] = useState([]);
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(true);
  
  // Modal State
  const [showModal, setShowModal] = useState(false);
  const [editRecord, setEditRecord] = useState(null);
  const [formData, setFormData] = useState({});

  const loadData = () => {
    setLoading(true);
    const params = query ? { search: query } : {};
    api.get(resource.path, { params })
      .then(res => setData(res.data.results || res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadData();
  }, [type, query]);

  const handleDelete = (id) => {
    if (!window.confirm("Are you sure you want to delete this record?")) return;
    api.delete(`${resource.path}${id}/`)
      .then(() => loadData())
      .catch(err => alert("Error deleting record"));
  };

  const openCreateModal = () => {
    const initialForm = {};
    resource.fields.forEach(f => initialForm[f] = '');
    setFormData(initialForm);
    setEditRecord(null);
    setShowModal(true);
  };

  const openEditModal = (record) => {
    const editForm = {};
    resource.fields.forEach(f => editForm[f] = record[f] || '');
    setFormData(editForm);
    setEditRecord(record);
    setShowModal(true);
  };

  const handleSave = (e) => {
    e.preventDefault();
    const req = editRecord 
      ? api.put(`${resource.path}${editRecord.id}/`, formData)
      : api.post(resource.path, formData);
      
    req.then(() => {
      setShowModal(false);
      loadData();
    }).catch(err => alert("Error saving record: " + JSON.stringify(err.response?.data || err.message)));
  };

  const renderCell = (key, value) => {
    if (value === null || value === undefined) return '—';
    if (typeof value === 'object') return JSON.stringify(value);
    
    if (key === 'status' || key === 'placement_status') {
      return <span className={`status-badge status-${String(value).replace(' ', '.')}`}>{value}</span>;
    }
    if (key === 'package') return `₹${Number(value).toFixed(2)} LPA`;
    return String(value);
  };

  return (
    <section>
      <div className="table-header">
        <div>
          <h2>{resource.title}</h2>
          <p className="subtitle">Manage {resource.title.toLowerCase()} via Live API</p>
        </div>
        <div style={{ display: 'flex', gap: '10px' }}>
          <input 
            className="search" 
            placeholder="Search records..." 
            value={query} 
            onChange={e => setQuery(e.target.value)}
          />
          <button className="btn-primary" onClick={openCreateModal}>+ Create New</button>
        </div>
      </div>

      <div className="tablewrap">
        {loading ? (
          <div className="empty">Loading {resource.title.toLowerCase()}...</div>
        ) : (
          <table>
            <thead>
              <tr>
                {resource.fields.map(f => (
                  <th key={f}>{f.replaceAll('_', ' ')}</th>
                ))}
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {data.map((row) => (
                <tr key={row.id}>
                  {resource.fields.map(f => (
                    <td key={f}>{renderCell(f, row[f])}</td>
                  ))}
                  <td>
                    <button className="btn-action edit" onClick={() => openEditModal(row)}>Edit</button>
                    <button className="btn-action delete" onClick={() => handleDelete(row.id)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
        {!loading && data.length === 0 && (
          <div className="empty">No records found.</div>
        )}
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>{editRecord ? 'Edit' : 'Create'} {resource.title.slice(0, -1)}</h3>
            <form onSubmit={handleSave}>
              <div className="form-grid">
                {resource.fields.map(f => (
                  <div className="form-group" key={f}>
                    <label>{f.replaceAll('_', ' ')}</label>
                    <input 
                      type={f.includes('date') ? 'date' : 'text'}
                      value={formData[f]}
                      onChange={e => setFormData({ ...formData, [f]: e.target.value })}
                      required={!f.includes('skills') && !f.includes('website')}
                    />
                  </div>
                ))}
              </div>
              <div className="modal-actions">
                <button type="button" className="btn-secondary" onClick={() => setShowModal(false)}>Cancel</button>
                <button type="submit" className="btn-primary">Save</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </section>
  );
}

export default CrudList;
