from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Group.

    Поддерживает только чтение:
        - список групп
        - получение одной группы

    Поля:
        id: идентификатор группы
        title: название группы
        slug: уникальный slug группы
        description: описание группы
    """

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Поддерживает:
        - получение списка постов (GET)
        - получение одного поста (GET)
        - создание поста (POST)
        - обновление и удаление (PUT, PATCH, DELETE)

    Поля:
        id: идентификатор поста
        text: текст поста
        author: автор поста
        image: изображение поста (опционально)
        group: группа поста (опционально, допустима передача null)
        pub_date: дата публикации
    """
    author = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(required=False)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.

    Поддерживает:
        - получение списка комментариев поста (GET)
        - получение одного комментария (GET)
        - создание комментария (POST)
        - обновление и удаление (PUT, PATCH, DELETE)

    Поля:
        id: идентификатор комментария
        author: автор комментария
        post: пост, к которому относится комментарий
        text: текст комментария
        created: дата создания
    """
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
