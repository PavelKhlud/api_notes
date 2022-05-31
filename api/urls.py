from django.urls import path, include
from rest_framework import routers

from api.views import NoteViewSet, UsersViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls), name='notes_viewset')
]
