from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import userapiviewset, Userview

router_user = DefaultRouter()
router_user .register(prefix = 'users', viewset= userapiviewset, basename= 'users')

urlpatterns = [
    path('auth/me', Userview.as_view() )
]
