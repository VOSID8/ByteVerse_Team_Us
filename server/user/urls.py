from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.ValidateRefugee.as_view(), name='validate'),
    path('role/', views.UserDesignation.as_view(), name='role'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]