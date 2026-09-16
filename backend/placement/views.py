from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.models import Avg, Max, Count, F
from django.db.models.functions import TruncMonth
from .models import *
from .serializers import *


class Base(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("search")
        if q:
            from django.db.models import Q

            fields = getattr(self, "search_fields", [])
            cond = Q()
            for f in fields:
                cond |= Q(**{f + "__icontains": q})
            qs = qs.filter(cond)
        return qs


class StudentViewSet(Base):
    queryset = Student.objects.all().order_by("-id")
    serializer_class = StudentSerializer
    search_fields = ["name", "student_id", "department", "skills"]


class CompanyViewSet(Base):
    queryset = Company.objects.all().order_by("company_name")
    serializer_class = CompanySerializer
    search_fields = ["company_name", "industry", "location"]


class DriveViewSet(Base):
    queryset = (
        PlacementDrive.objects.select_related("company").all().order_by("-drive_date")
    )
    serializer_class = DriveSerializer
    search_fields = ["job_role", "company__company_name", "required_skills"]


class ApplicationViewSet(Base):
    queryset = (
        Application.objects.select_related("student", "placement_drive__company")
        .all()
        .order_by("-application_date")
    )
    serializer_class = ApplicationSerializer
    search_fields = [
        "student__name",
        "placement_drive__company__company_name",
        "status",
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff and hasattr(
            self.request.user, "student_profile"
        ):
            qs = qs.filter(student=self.request.user.student_profile)
        return qs


class PlacementViewSet(Base):
    queryset = (
        Placement.objects.select_related("student", "company", "placement_drive")
        .all()
        .order_by("-placement_date")
    )
    serializer_class = PlacementSerializer
    search_fields = ["student__name", "company__company_name", "job_role"]


@api_view(["POST"])
@permission_classes([])
def login(request):
    u = authenticate(
        username=request.data.get("username"), password=request.data.get("password")
    )
    if not u:
        return Response({"detail": "Invalid credentials"}, status=400)
    t, _ = Token.objects.get_or_create(user=u)
    return Response(
        {
            "token": t.key,
            "username": u.username,
            "is_staff": u.is_staff,
            "student_id": getattr(getattr(u, "student_profile", None), "id", None),
        }
    )


@api_view(["GET"])
def overview(request):
    total = Student.objects.count()
    placed = Student.objects.filter(placement_status="Placed").count()
    return Response(
        {
            "total_students": total,
            "total_companies": Company.objects.count(),
            "active_drives": PlacementDrive.objects.filter(status="Open").count(),
            "total_applications": Application.objects.count(),
            "students_placed": placed,
            "placement_percentage": round(placed / total * 100, 2) if total else 0,
            "average_package": float(
                Placement.objects.aggregate(v=Avg("package"))["v"] or 0
            ),
            "highest_package": float(
                Placement.objects.aggregate(v=Max("package"))["v"] or 0
            ),
        }
    )


@api_view(["GET"])
def department_stats(request):
    out = []
    for d in Student.objects.values("department").annotate(total=Count("id")):
        p = Student.objects.filter(
            department=d["department"], placement_status="Placed"
        ).count()
        out.append(
            {
                "department": d["department"],
                "total": d["total"],
                "placed": p,
                "percentage": round(p / d["total"] * 100, 2) if d["total"] else 0,
            }
        )
    return Response(out)


@api_view(["GET"])
def company_stats(request):
    return Response(
        list(
            Placement.objects.values(name=F("company__company_name"))
            .annotate(hired=Count("id"))
            .order_by("-hired")
        )
    )


@api_view(["GET"])
def application_stats(request):
    return Response(
        list(Application.objects.values("status").annotate(count=Count("id")))
    )


@api_view(["GET"])
def placement_trends(request):
    return Response(
        list(
            Placement.objects.annotate(month=TruncMonth("placement_date"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )
    )
