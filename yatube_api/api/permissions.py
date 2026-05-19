from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Проверяет авторство контента.

    GET-запрос на получение списка объектов, отдельного объекта и POST-запрос
    на создание объекта разрешены только аутентифицированным пользователям.

    PUT, PATCH и DELETE запросы разрешены только автору контента.

    В случае отсутствия прав на редактирование - ошибка 403.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
