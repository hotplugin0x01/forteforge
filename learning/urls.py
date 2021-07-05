from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('enterprise/', views.signupEnterprise, name='signup_enterprise'),
    path('', views.login, name='login')
]
