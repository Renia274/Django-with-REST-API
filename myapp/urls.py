from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet

# Create a router object
router = routers.DefaultRouter()

# Register the CategoryViewSet with the router for the 'categories' URL pattern
router.register(r'categories', CategoryViewSet)

# Register the ProductViewSet with the router for the 'products' URL pattern
router.register(r'products', ProductViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs in the root URLconf
]
