"""swimming_gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from swimming_gym import settings
from student_management_app import views, hod_views

urlpatterns = [
    path('demo', views.show_demo_page),
    path('admin/', admin.site.urls),
    path('', views.show_login_page),
    path('get_user_details', views.get_user_details),
    path('logout_user', views.logout_user),
    path('do_login', views.do_login),
    path('admin_home', hod_views.admin_home),
    path('add_staff', hod_views.add_staff),
    path('add_staff_save', hod_views.add_staff_save)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
