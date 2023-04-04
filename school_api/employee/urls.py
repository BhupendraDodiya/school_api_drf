from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_get.as_view()),
    path('one/<int:pk>/',views.employee_one.as_view()),
    path('create/',views.employee_create.as_view()),
    path('update/<int:pk>/',views.employee_update.as_view()),
    path('delete/<int:pk>/',views.employee_delete.as_view()),
]
