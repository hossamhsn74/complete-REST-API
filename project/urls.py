from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialAccountListView, SocialAccountDisconnectView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


# class GithubLogin(SocialLoginView):
#     adapter_class = GitHubOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
#     client_class = OAuth2Client


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter


schema_view = get_schema_view(
    openapi.Info(
        title="Custom API",
        default_version='v1',
        description="This is my custom API, I use all basic functions in this REST API, thanks",
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
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/facebook/connect/', FacebookLogin.as_view(), name='fb_connect'),
    # path('rest-auth/github/connect/', GitHubLogin.as_view(), name='github_login'),
    # re_path(
    #     r'^rest-auth/socialaccounts/$',
    #     SocialAccountListView.as_view(),
    #     name='social_account_list'
    # ),
    # re_path(
    #     r'^rest-auth/socialaccounts/(?P<pk>\d+)/disconnect/$',
    #     SocialAccountDisconnectView.as_view(),
    #     name='social_account_disconnect'
    # ),

    # yasg swagger urls
    path('docs/', schema_view.with_ui('redoc',
                                     cache_timeout=0), name='schema-redoc'),
    # re_path(r'api/(?P<version>[v1|v2]+)/',
    #         include('bookstore.urls')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    #         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
