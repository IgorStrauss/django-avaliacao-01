from rest_framework.routers import DefaultRouter

from api.viewsets import CarViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'cars', CarViewSet, basename='cars')
urlpatterns = router.urls
