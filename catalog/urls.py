from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactTemplateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
]