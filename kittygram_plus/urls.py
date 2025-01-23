from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
