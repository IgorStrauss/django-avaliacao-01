from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import CarViewSet, PersonCarViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'person_car', PersonCarViewSet, basename='person-car')
urlpatterns = router.urls

urlpatterns = [
    path("persons/create/", PersonViewSet.as_view({'post': 'create'})),
    path("cars/create/", CarViewSet.as_view({'post': 'create'})),
    path("", include(router.urls))
]
