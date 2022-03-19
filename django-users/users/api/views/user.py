from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.api.permissions import IsPostOrAuthenticated
from users.api.serializers.user import (
    UserSerializer,
    UserEditSerializer,
    UserRegisterSerializer,
    UserChangePasswordSerializer)

User = get_user_model()


class UserViewset(ListModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = (IsPostOrAuthenticated,)

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        elif self.action == 'create':
            return UserRegisterSerializer
        else:
            return UserEditSerializer

    def list(self, request, *args, **kwargs):
        user = self.get_queryset()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()

    def perform_update(self, serializer):
        serializer.save()

    @action(detail=False, serializer_class=UserEditSerializer, methods=['patch'])
    def edit(self, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=self.request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=False, serializer_class=UserChangePasswordSerializer, methods=['patch'])
    def change_password(self, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        if authenticate(user=instance, password=serializer.validated_data.get('old_password')):
            instance.set_password(serializer.validated_data.get('new_password'))
            response = {
                'message': 'Password updated successfully.'
            }
            code = status.HTTP_202_ACCEPTED
        else:
            response = {
                'message': 'Password is not correct.'
            }
            code = status.HTTP_403_FORBIDDEN

        return Response(response, status=code)

