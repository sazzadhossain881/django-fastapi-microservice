from django.urls import path
from product import views

urlpatterns = [
    path("list/", views.ProductAPIView.as_view(), name='product-list'),
    path("list/<int:product_id>/", views.productRetrieveAPIView.as_view(), name='product-retrieve'),
    path("update/<int:product_id>/", views.ProductupdateAPIView.as_view(), name='product-update'),
    path("delete/<int:product_id>/", views.ProductDeleteAPIView.as_view(), name='product-delete'),
]
