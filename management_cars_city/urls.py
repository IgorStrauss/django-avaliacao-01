from django.urls import path

from . import views

app_name = "management_cars_city"

urlpatterns = [path("", views.index_first, name="index"),
               path("persons", views.persons, name='listar_pessoas'),
               path("oportunity", views.sales_opportunity,
                    name='oportunidade_venda'),
               path("owner", views.owners_car,
                    name='listar_carros_proprietarios'),
               path("register-car", views.CreateCar.as_view(),
                    name='register_car'),
               path("create-person", views.CreatePerson.as_view(),
                    name='create_person'),
               path("<int:pk>", views.sales_opportunity_id,
                    name='sales'),
               path("persons-cars/<int:person_id>", views.persons_cars, name='contagem')]
