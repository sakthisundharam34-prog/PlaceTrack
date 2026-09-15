from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id=models.CharField(max_length=30,unique=True); name=models.CharField(max_length=120); email=models.EmailField(unique=True); phone=models.CharField(max_length=20,blank=True)
    department=models.CharField(max_length=30); year=models.PositiveSmallIntegerField(); cgpa=models.DecimalField(max_digits=4,decimal_places=2); skills=models.TextField(blank=True); backlogs=models.PositiveIntegerField(default=0)
    placement_status=models.CharField(max_length=30,default='Not Placed'); user=models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL,related_name='student_profile'); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return f'{self.student_id} - {self.name}'
class Company(models.Model):
    company_name=models.CharField(max_length=150,unique=True); email=models.EmailField(blank=True); phone=models.CharField(max_length=20,blank=True); website=models.URLField(blank=True); industry=models.CharField(max_length=80); location=models.CharField(max_length=120); description=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.company_name
class PlacementDrive(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='drives'); job_role=models.CharField(max_length=120); package=models.DecimalField(max_digits=7,decimal_places=2); eligibility_cgpa=models.DecimalField(max_digits=4,decimal_places=2); eligible_departments=models.JSONField(default=list); drive_date=models.DateField(); application_deadline=models.DateField(); required_skills=models.TextField(blank=True); description=models.TextField(blank=True); status=models.CharField(max_length=20,default='Upcoming'); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return f'{self.company} - {self.job_role}'
class Application(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='applications'); placement_drive=models.ForeignKey(PlacementDrive,on_delete=models.CASCADE,related_name='applications'); application_date=models.DateTimeField(auto_now_add=True); status=models.CharField(max_length=20,default='Applied'); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: constraints=[models.UniqueConstraint(fields=['student','placement_drive'],name='unique_student_drive')]
class Placement(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='placements'); company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='placements'); placement_drive=models.ForeignKey(PlacementDrive,on_delete=models.CASCADE,related_name='placements'); job_role=models.CharField(max_length=120); package=models.DecimalField(max_digits=7,decimal_places=2); placement_date=models.DateField(); joining_date=models.DateField(null=True,blank=True); status=models.CharField(max_length=20,default='Placed'); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
