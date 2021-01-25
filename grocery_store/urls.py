"""grocery_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from grocery_store_app import views

urlpatterns = [
    path('this/is/my/admin/', admin.site.urls),
    path('home/', views.index, name = 'index'),
    path('add/', views.add, name = 'add'),
    path('update/', views.update, name = 'update'),
    path('delete/', views.delete, name = 'delete'),
    path('filter/', views.filter, name = 'filter'),
    path('', views.Login.as_view(), name = 'login'),
    path('register/', views.Register.as_view(), name = 'register'),
    path('logout/', views.logout, name = 'logout'),
]


