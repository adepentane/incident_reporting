from django.urls import path
from .views import search_results

app_name = 'search'

urlpatterns = [
    path('results/', search_results, name='search_results'),
]