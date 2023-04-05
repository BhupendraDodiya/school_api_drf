from django.urls import path
from student import views

urlpatterns = [
    path('',views.student_get.as_view()),
    path('one/<int:pk>/',views.student_one.as_view()),
    path('create/',views.student_create.as_view()),
    path('update/<int:pk>/',views.student_update.as_view()),
    path('delete/<int:pk>/',views.student_delete.as_view()),
]
