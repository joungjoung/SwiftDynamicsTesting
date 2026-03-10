from rest_framework import serializers

from .models import Classroom, School, Student, Teacher

class TeacherBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'sex']


class StudentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'sex']


class ClassroomBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'year_class', 'sub_class']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'nickname', 'address']


class SchoolDetailSerializer(SchoolSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + ['classroom_count', 'teacher_count', 'student_count']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'school', 'year_class', 'sub_class']


class ClassroomDetailSerializer(ClassroomSerializer):
    teachers = TeacherBriefSerializer(many=True, read_only=True)
    students = StudentBriefSerializer(many=True, read_only=True)

    class Meta(ClassroomSerializer.Meta):
        fields = ClassroomSerializer.Meta.fields + ['teachers', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'sex', 'classrooms']


class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassroomBriefSerializer(many=True, read_only=True)

    class Meta(TeacherSerializer.Meta):
        fields = ['id', 'name', 'surname', 'sex', 'classrooms']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'sex', 'classroom']


class StudentDetailSerializer(StudentSerializer):
    classroom = ClassroomBriefSerializer(read_only=True)

    class Meta(StudentSerializer.Meta):
        fields = ['id', 'name', 'surname', 'sex', 'classroom']