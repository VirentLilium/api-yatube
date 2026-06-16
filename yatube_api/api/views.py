"""ViewSet-классы для API приложения yatube."""

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.serializers import BaseSerializer

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для публикаций."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer: BaseSerializer) -> None:
        """
        Сохраняет новую публикацию с текущим пользователем в качестве автора.

        :param serializer: Сериализатор с валидированными данными.
        :return: None.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев к публикациям."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self) -> Post:
        """
        Возвращает публикацию из URL.

        :return: Объект публикации.
        :raises Http404: Если публикация не найдена.
        """
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self) -> QuerySet:
        """
        Возвращает комментарии текущей публикации.

        :return: QuerySet комментариев публикации.
        """
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer: BaseSerializer) -> None:
        """
        Сохраняет новый комментарий к текущей публикации.

        Автором комментария становится текущий пользователь.

        :param serializer: Сериализатор с валидированными данными.
        :return: None.
        """
        serializer.save(
            author=self.request.user,
            post=self.get_post(),
        )
