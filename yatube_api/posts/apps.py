"""Конфигурация приложения posts."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Конфигурация приложения posts."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Посты блога'
