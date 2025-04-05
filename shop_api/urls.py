from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryList, CategoryDetail,
    ProductList, ProductDetail,
    ReviewList, ReviewDetail,
    ProductWithReviewsView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', CategoryList.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryDetail.as_view()),
    path('api/v1/products/', ProductList.as_view()),
    path('api/v1/products/<int:pk>/', ProductDetail.as_view()),
    path('api/v1/products/reviews/', ProductWithReviewsView.as_view()),  # <--- добавили
    path('api/v1/reviews/', ReviewList.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetail.as_view()),
]
