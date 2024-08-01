# reports/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reports', views.ReportViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'videos', views.VideoViewSet)

app_name = 'reports'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.report_create, name='report_create'),
    path('update/<slug:slug>/', views.report_update, name='report_update'),
    path('delete/<slug:slug>/', views.report_delete, name='report_delete'),
    path('list/', views.report_list, name='report_list'),
    path('detail/<slug:slug>/', views.report_detail, name='report_detail'),
]
