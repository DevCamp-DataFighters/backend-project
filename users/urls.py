
from django.urls import path

from .views import Student_RegisterView, Teacher_RegisterView, Admin_RegisterView
from .views import Custom_Auth_Token, LogoutView

urlpatterns = [

    path('register/student', Student_RegisterView.as_view(),
         name='student_register'),

    path('register/teacher', Teacher_RegisterView.as_view(),
         name='teacher_register'),

    path('register/admin', Admin_RegisterView.as_view(),
         name='admin_register'),

    path('login', Custom_Auth_Token.as_view(),
         name='Auth-token'),

    path('logout', LogoutView.as_view(),
         name='logout'),


]
