from django.urls import path
from . import views

app_name = "data"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("profiles/", views.ProfileList.as_view(), name="profiles"),
    path("create-profile/", views.ProfileCreate.as_view(), name="create-profile"),
    path("watch-list/<str:profile_id>/", views.WatchList.as_view(), name="watch-list"),

]
