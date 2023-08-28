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

# 2. Multitable Inheritance


class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)


class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()

# 3.proxy model


class Friend(models.Model):
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)


# one to one relationship
class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']


class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name


class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()


# one to many relationship
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    created_at = models.DateTimeField()
# many to many relationship


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)

    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
