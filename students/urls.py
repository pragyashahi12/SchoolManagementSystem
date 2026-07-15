from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path("add/", views.add_student, name="add_student"),
    path("edit/<int:id>/", views.edit_student, name="edit_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    path('email-form/', views.email_form, name='email_form'),
    path('send-email/',views.sendEmail),
]