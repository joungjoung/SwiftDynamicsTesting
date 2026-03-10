from rest_framework.viewsets import ModelViewSet

from ...filters import StudentFilter
from ...models import Student
from ...serializers import StudentDetailSerializer, StudentSerializer


class StudentViewSet(ModelViewSet):
    filterset_class = StudentFilter

    def get_queryset(self):
        return Student.objects.select_related('classroom', 'classroom__school')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer
