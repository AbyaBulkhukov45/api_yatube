from rest_framework.exceptions import PermissionDenied


class UpdateDestroyMixin:
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Нельзя редактировать, у тебя нет прав!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Нельзя удалять, у тебя нет прав!')
        super().perform_destroy(instance)
