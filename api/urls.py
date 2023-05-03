from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ListPersonWithoutStatusOwnerCar,
                       ListPersonWithStatusOwnerCar)
from api.viewsets import CarViewSet, PersonCarViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'person_car', PersonCarViewSet, basename='person-car')
urlpatterns = router.urls

urlpatterns = [
    path("persons/create/", PersonViewSet.as_view({'post': 'create'})),
    path("cars/create/", CarViewSet.as_view({'post': 'create'})),
    path("persons/owner/true/", ListPersonWithStatusOwnerCar.as_view()),
    path("persons/owner/false/", ListPersonWithoutStatusOwnerCar.as_view(),
         name='Oportunidade de vendas'),
    path("", include(router.urls))
]
