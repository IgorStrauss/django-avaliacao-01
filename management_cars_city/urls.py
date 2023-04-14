from django.urls import path

from . import views

app_name = "management_cars_city"

urlpatterns = [path("", views.index_first, name="index"),
               path("persons", views.persons, name='listar_pessoas'),
               path("oportunity", views.sales_opportunity,
                    name='listar_oportunidade_vendas'),
               path("owner", views.owner_car,
                    name='listar_carros_proprietarios')]
