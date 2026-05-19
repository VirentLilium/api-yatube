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
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug группы'
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )

    def __str__(self):
        return self.title[:30]


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
    text = models.TextField(
        verbose_name='Текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа поста'
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:30]


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
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления комментария'
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'{self.text[:30]} | {self.author.username}, пост "{self.post}"'
