# 🎓 PlaceTrack – College Placement Management System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![React](https://img.shields.io/badge/React-18.x-blue?logo=react)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![Status](https://img.shields.io/badge/Status-Active-success)

> **Connect Students. Careers. Companies.**

PlaceTrack is a comprehensive, full-stack college placement management application built to streamline the recruitment process for educational institutions. It seamlessly connects students, recruiters (companies), and placement coordinators through a robust and intuitive platform.

---

## ✨ Key Features

- **Role-Based Authentication**: Secure access for students, coordinators, and administrators.
- **Student Profiles & Management**: Maintain comprehensive academic records and tracking.
- **Company & Drive Management**: Organize and track placement drives, including eligibility criteria.
- **Live Applications & Eligibility**: Automated checking of student eligibility against company requirements before applying.
- **Placement Tracking**: End-to-end tracking from application to final placement offers.
- **Advanced Analytics Dashboard**: Real-time insights with statistical breakdowns for departments, companies, and placement trends.
- **Search & Filtering**: Powerful tools to filter students, drives, and applications based on multiple criteria.

---

## 🛠️ Technology Stack

**Frontend:**
- [React.js](https://reactjs.org/)
- [Vite](https://vitejs.dev/) (Build tool)
- [Axios](https://axios-http.com/) (API Client)
- [React Router](https://reactrouter.com/) (Navigation)
- Modern CSS (Custom styling and layouts)

**Backend:**
- [Django](https://www.djangoproject.com/) (Python Web Framework)
- [Django REST Framework](https://www.django-rest-framework.org/) (API Architecture)
- [SQLite](https://www.sqlite.org/) (Database)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) (CORS Management)

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Node.js](https://nodejs.org/) (v16+ recommended)
- [Python](https://www.python.org/) (3.10+ recommended)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/sakthisundharam34-prog/PlaceTrack.git
```

### 2. Backend Setup

Open a terminal and navigate to the `backend` directory:

```bash
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create an admin/superuser (Optional but recommended)
python manage.py createsuperuser

# Start the Django development server
python manage.py runserver
```

The backend server will be running on `http://127.0.0.1:8000/`.

### 3. Frontend Setup

Open a new terminal and navigate to the `frontend` directory:

```bash
cd frontend

# Install Node dependencies
npm install

# Start the Vite development server
npm run dev
```

The frontend application will be available at `http://localhost:5173/`.

---

## 📡 API Reference

The backend exposes a comprehensive RESTful API under the `/api/` prefix.

**Authentication & Core Data:**
- `POST /api/auth/login/` - User authentication
- `GET/POST/PUT/DELETE /api/students/` - Student CRUD operations
- `GET/POST/PUT/DELETE /api/companies/` - Company management
- `GET/POST/PUT/DELETE /api/drives/` - Placement drive coordination

**Applications & Placements:**
- `GET/POST/PUT/DELETE /api/applications/` - Track student applications
- `GET/POST/PUT/DELETE /api/placements/` - Manage final placement records

**Analytics (Read-Only):**
- `GET /api/analytics/overview/` - High-level metrics
- `GET /api/analytics/department-stats/` - Departmental performance
- `GET /api/analytics/company-stats/` - Company recruitment stats
- `GET /api/analytics/application-stats/` - Application funnel data
- `GET /api/analytics/placement-trends/` - Historical placement trends

---

## 🏗️ Architecture & Database

- **Flow**: React (Client) → Axios (HTTP) → DRF (API Views) → Django ORM → SQLite.
- **Relational Integrity**: The database schema strictly enforces foreign key relationships between `Student`, `Company`, `PlacementDrive`, `Application`, and `Placement`.
- **Constraint Safety**: Prevents duplicate applications to the same drive using robust database-level `UniqueConstraint` validations.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
