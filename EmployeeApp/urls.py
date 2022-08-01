from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('department/', views.department_api),
    path('department/<int:pk>/', views.department_api)
]
