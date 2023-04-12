from django.urls import path

from . import views

app_name = "management_cars_city"

urlpatterns = [path("", views.index, name="Index")]
