from django.db import models

# Create your models here.
class Course(models.Model):
    #code = attribute
    #auto primary key = (id=auto)
    code = models.CharField(max_length = 4, primary_key = True)
    description = models. TextField()

class Student(models.Model):
    id = models.CharField(max_length = 12, primary_key = True)
    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length = 12)
    course_code = models.ForeignKey(Course, on_delete = models.CASCADE)
    status = models.CharField(max_length = 8, default = "Active")
    