"""drf_api URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(profiles.urls))
]

"""
Continue lesson: 
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/b50f474f85af4de69944fa15a1342abd/9e0bea8f758944059ede7f1fc5ac694a/?child=first
Lesson 1
3:20
"""