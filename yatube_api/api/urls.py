from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view(
            {'get': 'list',
             'post': 'create'}
        ),
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view(
            {'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'}
        ),
    ),
    path('api-token-auth/', obtain_auth_token),
]
