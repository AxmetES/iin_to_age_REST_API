from django.urls import path, include
from rest_framework.routers import DefaultRouter

from iin_to_age.views import PersonViewSetApi

router = DefaultRouter()
router.register(r'people', PersonViewSetApi, basename='people')
urlpatterns = [
    path('', include(router.urls)),
]
