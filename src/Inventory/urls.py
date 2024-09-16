from django.urls import path
from .views import ProductsView,ProductsViewId

urlpatterns = [
    path('products/',ProductsView.as_view(),name="products"),
    path('products_view/<int:id>/',ProductsViewId.as_view(),name="products_id")
]

