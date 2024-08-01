from .views import home, category_detail, about_us
from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'frontend'

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('about/', about_us, name='about_us'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls', namespace='users')),
]