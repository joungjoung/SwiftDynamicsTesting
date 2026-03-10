from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from ...filters import SchoolFilter
from ...models import School
from ...serializers import SchoolDetailSerializer, SchoolSerializer

class SchoolViewSet(ModelViewSet):
    filterset_class = SchoolFilter

    def get_queryset(self):
        return School.objects.annotate(
            classroom_count=Count('classrooms', distinct=True),
            teacher_count=Count('classrooms__teachers', distinct=True),
            student_count=Count('classrooms__students', distinct=True),
        )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolSerializer