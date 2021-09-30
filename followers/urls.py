from django.urls import path
from . import views

urlpatterns = [
    path("followers/", views.FollowerList.as_view()),
    path("followers/<pk>/", views.FollowerDetail.as_view())
]
