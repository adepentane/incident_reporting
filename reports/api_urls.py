from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, ImageViewSet, VideoViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'images', ImageViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = router.urls