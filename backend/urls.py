from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import UserViewSet, CustomTokenObtainPairView, TaskViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),  # includes /api/users/
    path('api/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
