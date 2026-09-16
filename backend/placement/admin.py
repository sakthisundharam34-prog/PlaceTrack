from django.contrib import admin
from .models import *
for m in [Student,Company,PlacementDrive,Application,Placement]: admin.site.register(m)
