"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from .views import home_view, about_view, student_delete, student_list, student_add, student_detail

urlpatterns = [
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('list/', student_list, name="list"),
    path('add/', student_add, name="add"),
    path('<int:id>/detail/', student_detail, name="detail"),
    path('<int:id>/delete', student_delete, name="delete")
]
