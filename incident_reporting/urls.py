from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from frontend.views import home, about_us, category_detail
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

schema_view = get_schema_view(
    openapi.Info(
        title="Incident Reporting API",
        default_version='v1',
        description="API documentation for the Incident Reporting project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('api/users/', include('users.api_urls')),
    path('categories/', include('categories.urls', namespace='categories')),
    path('api/categories/', include('categories.api_urls')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('api/reports/', include('reports.api_urls')),
    path('', home, name='home'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('about/', about_us, name='about_us'),
    path('logout/', include('frontend.urls', namespace='frontend')),  # Ensure this is correct
    path('api/frontend/', include('frontend.api_urls', namespace='frontend')),
    path('search/', include('search.urls', namespace='search')),
    path('api/search/', include('search.api_urls')),
    # Uncomment the next lines if you have swagger or redoc views
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)