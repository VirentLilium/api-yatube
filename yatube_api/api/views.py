from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from posts.models import Comment, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Post.

    Позволяет:
        - получать список постов (GET)
        - получать отдельный пост (GET)
        - создавать пост (POST)
        - обновлять пост (PUT, PATCH)
        - удалять пост (DELETE)

    Доступ:
        - только аутентифицированные пользователи могут использовать API
        - изменение и удаление поста разрешено только автору
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для модели Group.

    Позволяет:
        - получать список групп (GET)
        - получать информацию о группе (GET)

    Доступ:
        - только аутентифицированные пользователи
        - изменение и создание групп запрещены
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Comment.

    Комментарии привязаны к конкретному посту.

    Позволяет:
        - получать список комментариев поста (GET)
        - получать конкретный комментарий (GET)
        - создавать комментарий к посту (POST)
        - редактировать комментарий (PUT, PATCH)
        - удалять комментарий (DELETE)

    Доступ:
        - только аутентифицированные пользователи
        - изменение и удаление разрешено только автору комментария
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(
            author=self.request.user,
            post=post
        )
