from django.urls import path
# from . import views
from .api import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name=None),
    path('create/', views.ProductCreateView.as_view(), name=None),
    path('<int:pk>/', views.ProductDetailView.as_view(), name=None),

]
