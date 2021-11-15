from rest_framework import viewsets

from posts.models import User

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
