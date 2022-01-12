from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("posts/", views.IndexView.as_view(), name="index"),
    path("posts/<slug:slug>", views.DetailView.as_view(), name="details"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("about", views.AboutView.as_view(), name="about")
]