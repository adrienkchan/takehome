from django.urls import path
from .views import employee_list, employee_show

urlpatterns = [
    path("", employee_list, name="list_create_employees"),
    path("<int:pk>/", employee_show, name="get_del_put_employee"),
]
