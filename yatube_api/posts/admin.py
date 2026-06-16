"""Настройки административной панели для приложения posts."""

from django.contrib import admin

from posts.models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройки отображения постов в административной панели."""

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = (
        'text',
        'author__username',
        'group__title',
    )
    list_filter = (
        'pub_date',
        'group',
    )
    list_select_related = (
        'author',
        'group',
    )
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Настройки отображения групп в административной панели."""

    list_display = (
        'pk',
        'title',
        'slug',
    )
    search_fields = (
        'title',
        'slug',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройки отображения комментариев в административной панели."""

    list_display = (
        'pk',
        'text',
        'post',
        'author',
        'created',
    )
    search_fields = (
        'text',
        'author__username',
        'post__text',
    )
    list_filter = (
        'created',
    )
    list_select_related = (
        'author',
        'post',
    )
    empty_value_display = '-пусто-'
