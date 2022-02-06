from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>/", views.PostDatail.as_view()),
]
