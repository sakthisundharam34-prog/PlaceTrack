from rest_framework import serializers
from .models import *
class StudentSerializer(serializers.ModelSerializer):
 class Meta: model=Student; fields='__all__'
 def validate(self,d):
  if not 0<=float(d['cgpa'])<=10: raise serializers.ValidationError({'cgpa':'CGPA must be between 0 and 10.'})
  if d['year'] not in range(1,5): raise serializers.ValidationError({'year':'Year must be 1 to 4.'})
  return d
class CompanySerializer(serializers.ModelSerializer):
 class Meta: model=Company; fields='__all__'
class DriveSerializer(serializers.ModelSerializer):
 company_name=serializers.CharField(source='company.company_name',read_only=True)
 class Meta: model=PlacementDrive; fields='__all__'; extra_fields=['company_name']
class ApplicationSerializer(serializers.ModelSerializer):
 student_name=serializers.CharField(source='student.name',read_only=True); company=serializers.CharField(source='placement_drive.company.company_name',read_only=True); job_role=serializers.CharField(source='placement_drive.job_role',read_only=True)
 class Meta: model=Application; fields=['id','student','placement_drive','application_date','status','created_at','updated_at','student_name','company','job_role']
 def validate(self,d):
  s=d['student']; drive=d['placement_drive']
  if float(s.cgpa)<float(drive.eligibility_cgpa) or (drive.eligible_departments and s.department not in drive.eligible_departments) or s.backlogs>0: raise serializers.ValidationError('Student does not meet eligibility requirements.')
  return d
class PlacementSerializer(serializers.ModelSerializer):
 class Meta: model=Placement; fields='__all__'
