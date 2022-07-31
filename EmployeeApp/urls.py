from django.urls import include, re_path
from EmployeeApp import views

urlpatterns = [
    re_path(r'^department$', views.department_api),
    re_path(r'^department/([0-9]+)$', views.department_api)
]
