from django.urls import path, include
from .views import MenuItemViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'', MenuItemViewSet)
#urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
]