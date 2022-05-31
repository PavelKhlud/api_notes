from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from accounts.models import User
from api.serializers import NoteSerializer, UserSerializer
from .permissions import IsAuthor
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = get_user_model()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            if self.request.user.is_authenticated and self.request.user.is_admin:
                self.permission_classes = [IsAdminUser]
            else:
                self.permission_classes = [IsAuthor]
        elif self.action in ['list']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['create']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()