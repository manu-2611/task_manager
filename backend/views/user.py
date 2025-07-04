# backend/views.py
from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from backend.serializers.user import UserSerializer
User = get_user_model()

class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
