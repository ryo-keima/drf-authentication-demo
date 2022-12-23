from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'account', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]