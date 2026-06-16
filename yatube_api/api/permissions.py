"""Права доступа для API приложения yatube."""

from typing import Any

from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAuthorOrReadOnly(BasePermission):
    """Разрешает изменение объекта только его автору."""

    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: Any,
    ) -> bool:
        """
        Проверяет права пользователя на объект.

        Безопасные методы доступны всем авторизованным пользователям.
        Изменение и удаление объекта разрешены только автору контента.

        :param request: Объект HTTP-запроса.
        :param view: View, в котором выполняется проверка.
        :param obj: Проверяемый объект.
        :return: True, если доступ разрешён.
        """
        return request.method in SAFE_METHODS or obj.author == request.user
