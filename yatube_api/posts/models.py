"""Модели приложения posts."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_STR_LENGTH = 30


class Group(models.Model):
    """Группа публикаций."""

    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Slug группы',
    )
    description = models.TextField(
        verbose_name='Описание группы',
    )

    class Meta:
        """Настройки модели группы."""

        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        """
        Возвращает строковое представление группы.

        :return: Название группы.
        """
        return self.title[:MAX_STR_LENGTH]


class Post(models.Model):
    """Публикация пользователя."""

    text = models.TextField(
        verbose_name='Текст поста',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа поста',
    )

    class Meta:
        """Настройки модели публикации."""

        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        """
        Возвращает строковое представление публикации.

        :return: Текст публикации.
        """
        return self.text[:MAX_STR_LENGTH]


class Comment(models.Model):
    """Комментарий к публикации."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления комментария',
    )

    class Meta:
        """Настройки модели комментария."""

        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self) -> str:
        """
        Возвращает строковое представление комментария.

        :return: Текст комментария, автор и публикация.
        """
        return (
            f'{self.text[:MAX_STR_LENGTH]} | '
            f'{self.author.username}, пост "{self.post}"'
        )
