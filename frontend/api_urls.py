# frontend/api_urls.py
from django.urls import path
from .views import ActiveCategoryList

app_name = 'frontend'

urlpatterns = [
    path('active-categories/', ActiveCategoryList.as_view(), name='active_category_list'),
]
