
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home, name="homepage"),
    path("addemp/", add_emp, name="add_employee"),
    path('emplist/', emp_list, name="employee_list"),
    path('delete_emp/', delete_emp, name="delete_employee"),
    path('update_emp/<int:id>/', update_emp, name="update_emp")

    ]