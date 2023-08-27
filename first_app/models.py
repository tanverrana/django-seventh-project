from django.db import models

# Create your models here.


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return f"Roll :{self.roll}- {self.name}"
# Module Inheritance
# 1. Abstract base class
# 2. Multitable Inheritance
# 3. Proxy model

# 1. Abstract base class


class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    class Meta:
        abstract = True


class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)


class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
