# PlaceTrack – Placement Management System

**Connect Students. Careers. Companies.**

A full-stack college placement management application using React + Vite, Django REST Framework and SQLite. The requested specification requires live CRUD, authentication, eligibility checking, applications, placements, search/filtering and database-backed analytics.

## Run

### Backend
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:5173.

## API
- POST `/api/auth/login/`
- CRUD `/api/students/`, `/api/companies/`, `/api/drives/`, `/api/applications/`, `/api/placements/`
- Analytics `/api/analytics/overview/`, `/api/analytics/department-stats/`, `/api/analytics/company-stats/`, `/api/analytics/application-stats/`, `/api/analytics/placement-trends/`

## Architecture
React → Axios → Django REST Framework → Django ORM → SQLite.

## Database
Student, Company, PlacementDrive, Application and Placement are related with foreign keys; duplicate applications are prevented with a database UniqueConstraint.

## GitHub
```bash
git init
git add .
git commit -m "Build PlaceTrack placement management system"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```
