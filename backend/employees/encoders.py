from common.encoders import ModelEncoder
from .models import Employee

class EmployeeEncoder(ModelEncoder):
    model = Employee
    properties = [
        "first_name",
        "last_name",
        "email",
        "telephone",
        "bio",
        "union_member",
        "id",
    ]
