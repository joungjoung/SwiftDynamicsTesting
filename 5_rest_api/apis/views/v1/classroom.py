from rest_framework.viewsets import ModelViewSet

from ...filters import ClassroomFilter
from ...models import Classroom
from ...serializers import ClassroomDetailSerializer, ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    filterset_class = ClassroomFilter

    def get_queryset(self):
        return Classroom.objects.select_related('school').prefetch_related('teachers', 'students')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomSerializer