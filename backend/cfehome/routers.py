from rest_framework.routers import DefaultRouter


from products.viewsets import ProductGenericViewSet, ProductViewSet

router = DefaultRouter()
# router.register("products", ProductViewSet, basename="products")
router.register("products", ProductGenericViewSet, basename="products")
urlpatterns = router.urls
