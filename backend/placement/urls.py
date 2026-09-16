from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter(); router.register('students',StudentViewSet); router.register('companies',CompanyViewSet); router.register('drives',DriveViewSet); router.register('applications',ApplicationViewSet); router.register('placements',PlacementViewSet)
urlpatterns=[path('',include(router.urls)),path('auth/login/',login),path('analytics/overview/',overview),path('analytics/department-stats/',department_stats),path('analytics/company-stats/',company_stats),path('analytics/application-stats/',application_stats),path('analytics/placement-trends/',placement_trends)]
