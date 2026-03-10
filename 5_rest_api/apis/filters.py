from django_filters import FilterSet, filters

from .models import Classroom, School, Student, Teacher


class SchoolFilter(FilterSet):
	name = filters.CharFilter(field_name='name', lookup_expr='icontains')

	class Meta:
		model = School
		fields = ['name']


class ClassroomFilter(FilterSet):
	school = filters.NumberFilter(field_name='school_id')

	class Meta:
		model = Classroom
		fields = ['school']


class TeacherFilter(FilterSet):
	school = filters.NumberFilter(field_name='classrooms__school_id')
	classroom = filters.NumberFilter(field_name='classrooms__id')
	firstname = filters.CharFilter(field_name='name', lookup_expr='icontains')
	last_name = filters.CharFilter(field_name='surname', lookup_expr='icontains')
	lastname = filters.CharFilter(field_name='surname', lookup_expr='icontains')
	gender = filters.CharFilter(field_name='sex', lookup_expr='iexact')

	class Meta:
		model = Teacher
		fields = ['school', 'classroom', 'firstname', 'last_name', 'lastname', 'gender']


class StudentFilter(FilterSet):
	school = filters.NumberFilter(field_name='classroom__school_id')
	classroom = filters.NumberFilter(field_name='classroom_id')
	firstname = filters.CharFilter(field_name='name', lookup_expr='icontains')
	last_name = filters.CharFilter(field_name='surname', lookup_expr='icontains')
	lastname = filters.CharFilter(field_name='surname', lookup_expr='icontains')
	gender = filters.CharFilter(field_name='sex', lookup_expr='iexact')

	class Meta:
		model = Student
		fields = ['school', 'classroom', 'firstname', 'last_name', 'lastname', 'gender']
