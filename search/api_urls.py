from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SearchQueryViewSet

router = DefaultRouter()
router.register(r'search-queries', SearchQueryViewSet)

urlpatterns = router.urls