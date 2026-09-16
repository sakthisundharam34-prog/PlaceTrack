import os
import django
import random
from datetime import timedelta, date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from placement.models import Student, Company, PlacementDrive, Application, Placement
from django.contrib.auth import get_user_model

User = get_user_model()

departments = ['Computer Science', 'Information Technology', 'Electronics', 'Mechanical', 'Civil']
industries = ['Software', 'Fintech', 'Consulting', 'Core Engineering']
roles = ['Software Engineer', 'Data Analyst', 'Frontend Developer', 'System Engineer', 'Business Analyst']

def seed():
    print("Clearing old data...")
    Student.objects.all().delete()
    Company.objects.all().delete()
    PlacementDrive.objects.all().delete()
    Application.objects.all().delete()
    Placement.objects.all().delete()

    print("Creating Companies...")
    companies = []
    for i in range(15):
        c = Company.objects.create(
            company_name=f"Company {i+1}",
            email=f"hr@company{i+1}.com",
            phone=f"9876543{i:03d}",
            website=f"https://company{i+1}.com",
            industry=random.choice(industries),
            location=random.choice(["Bangalore", "Hyderabad", "Pune", "Chennai", "Gurgaon"]),
            description=f"A leading {random.choice(industries)} company."
        )
        companies.append(c)

    print("Creating Students...")
    students = []
    for i in range(100):
        username = f"student{i+1}"
        u, _ = User.objects.get_or_create(username=username, defaults={'email': f"{username}@college.edu"})
        s = Student.objects.create(
            student_id=f"STU2026{i:03d}",
            name=f"Student {i+1}",
            email=u.email,
            phone=f"9998887{i:03d}",
            department=random.choice(departments),
            year=2026,
            cgpa=round(random.uniform(6.0, 9.8), 2),
            skills="Python, React, Django",
            backlogs=random.choice([0, 0, 0, 0, 1, 2]),
            placement_status="Not Placed",
            user=u
        )
        students.append(s)

    print("Creating Placement Drives...")
    drives = []
    for i in range(20):
        d = PlacementDrive.objects.create(
            company=random.choice(companies),
            job_role=random.choice(roles),
            package=round(random.uniform(4.0, 24.0), 2),
            eligibility_cgpa=round(random.uniform(6.5, 8.0), 2),
            eligible_departments=random.sample(departments, k=random.randint(2, 5)),
            drive_date=date.today() + timedelta(days=random.randint(-30, 30)),
            application_deadline=date.today() + timedelta(days=random.randint(-40, 20)),
            required_skills="Good logic, communication",
            status=random.choice(['Upcoming', 'Ongoing', 'Completed'])
        )
        drives.append(d)

    print("Creating Applications & Placements...")
    for drive in drives:
        eligible_students = [s for s in students if s.cgpa >= drive.eligibility_cgpa and s.department in drive.eligible_departments and s.placement_status == 'Not Placed']
        applicants = random.sample(eligible_students, min(len(eligible_students), random.randint(5, 20)))
        
        for app_stu in applicants:
            Application.objects.create(
                student=app_stu,
                placement_drive=drive,
                status=random.choice(['Applied', 'Shortlisted', 'Rejected', 'Selected'])
            )
            
            # 20% chance to actually place them if the drive is completed
            if drive.status == 'Completed' and random.random() < 0.2 and app_stu.placement_status == 'Not Placed':
                Placement.objects.create(
                    student=app_stu,
                    company=drive.company,
                    placement_drive=drive,
                    job_role=drive.job_role,
                    package=drive.package,
                    placement_date=drive.drive_date,
                    status='Placed'
                )
                app_stu.placement_status = 'Placed'
                app_stu.save()

    print("Database seeding completed successfully.")

if __name__ == "__main__":
    seed()
