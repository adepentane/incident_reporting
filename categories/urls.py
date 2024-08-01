from django.urls import path
from .views import category_detail, category_list
from . import views

app_name = 'categories'

urlpatterns = [
    path('', category_list, name='category_list'),
    #path('<int:pk>/', category_detail, name='category_detail'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
]