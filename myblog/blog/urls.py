from django.urls import path
from . import views

urlpatterns = [
    path("mahmut/", views.index, name="index"),
    path("blog/",views.blogpage,name="blogpage")
]