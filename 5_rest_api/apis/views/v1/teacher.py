from rest_framework.viewsets import ModelViewSet

from ...filters import TeacherFilter
from ...models import Teacher
from ...serializers import TeacherDetailSerializer, TeacherSerializer


class TeacherViewSet(ModelViewSet):
    filterset_class = TeacherFilter

    def get_queryset(self):
        return Teacher.objects.prefetch_related('classrooms', 'classrooms__school').distinct()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherSerializer
