from rest_framework.routers import DefaultRouter
from django.urls import path, include
from products.views import ProductViewSet, CategoryViewSet, CafeViewSet, CategoryEatViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('cafes', CafeViewSet)
router.register('categoryeats', CategoryEatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]