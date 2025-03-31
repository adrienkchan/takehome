from .encoders import EmployeeEncoder
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.db.utils import IntegrityError
from .models import Employee
import json

# Create your views here.

@require_http_methods(["GET", "POST"])
def employee_list(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        return JsonResponse(
            {"employees" : employee},
            encoder=EmployeeEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            employee = Employee.objects.create(**content)
        except IntegrityError:
            return JsonResponse(
                {"message": "Unable to create"},
                status=400
            )
        return JsonResponse(
            employee,
            encoder=EmployeeEncoder,
            safe=False,
        )

@require_http_methods(["GET", "DELETE", "PUT"])
def employee_show(request, pk):
    if request.method == "GET":
        try:
            employee = Employee.objects.get(id=pk)
            return JsonResponse(
                employee,
                encoder=EmployeeEncoder,
                safe=False
            )
        except Employee.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Employee id"},
                status=404
            )
    elif request.method == "DELETE":
        try:
            Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Employee id"},
                status=404
            )
        count, _ = Employee.objects.get(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Employee id"},
                status=404
            )
        for key, value in content.items():
            setattr(employee, key, value)
        employee.save()
        
        return JsonResponse(
            employee,
            encoder=EmployeeEncoder,
            safe=False,
        )
