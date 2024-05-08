from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
