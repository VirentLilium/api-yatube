from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """
    Модель группы.

    Атрибуты:
        title (str): Заголовок группы.
        slug (slug): Слаг группы.
        description (str): Описание группы.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Модель публикации (пост) для блога.

    Атрибуты:
        text (str): Текст поста.
        pub_date (datetime): Дата и время публикации.
        author (User): Пользователь, создавший пост.
        image (ImageField | None): Опциональное изображение поста.
        group (Group | None): Группа, опциональное поле.
    """
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """
    Модель комментария к посту.

    Атрибуты:
        author (User): Пользователь, написавший комментарий.
        post (Post): Пост.
        text (str): Текст комментария.
        created (datetime): Дата и время добавления комментария.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )
