"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from operation.views import HelloworldView,HelloView,AddView,NumberView,GreetView,FormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloworldView.as_view()),
    path('home/', HelloView.as_view()),
    path('add/', AddView.as_view()),
    path('num/', NumberView.as_view()),
    path('greet/', GreetView.as_view()),
    path('form/', FormView.as_view())
]
# python manage.py startapp application_name 