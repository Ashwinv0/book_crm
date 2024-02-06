"""
URL configuration for employe project.

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
from work.views import Employe,BookView,Booklist,Book_DetailView,Book_Delete,StudentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",Employe.as_view()),
    path("book/",BookView.as_view()),
    path('book/all',Booklist.as_view(),name="book-al"),
    path("book/<int:pk>",Book_DetailView.as_view(),name="book-det"),
    path("book/<int:pk>/remove",Book_Delete.as_view(),name="book-del"),
    path("student/",StudentsView.as_view()),
]
