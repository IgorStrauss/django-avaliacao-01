from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.viewsets import CarViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'cars', CarViewSet, basename='cars')
urlpatterns = router.urls

urlpatterns = [
    path("persons/create/", PersonViewSet.as_view({'post': 'create'})),
    path("cars/create/", CarViewSet.as_view({'post': 'create'})),
    path("", include(router.urls))
]
