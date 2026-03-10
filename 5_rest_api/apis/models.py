from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    year_class = models.CharField(max_length=20)
    sub_class = models.CharField(max_length=20)

    def __str__(self):
        return self.year_class + "/" + self.sub_class

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', blank=True)

    def __str__(self):
        return self.name + " " + self.surname

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name + " " + self.surname
