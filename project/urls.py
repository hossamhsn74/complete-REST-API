from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Custom API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hossamhsn74@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="homepage"),
    path('bookstore/', include('bookstore.urls')),
    path('products/', include('products.urls')),

    # all-auth urls
    # path('rest-auth/', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),

    # yasg swagger urls
    path('doc/', schema_view.with_ui('redoc',
                                     cache_timeout=0), name='schema-redoc'),
    # re_path(r'api/(?P<version>[v1|v2]+)/',
    #         include('bookstore.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
