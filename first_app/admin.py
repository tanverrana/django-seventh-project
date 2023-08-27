from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel, Friend, Me
# Register your models here.
admin.site.register(StudentModel)
# admin.site.register(StudentInfoModel)
# admin.site.register(TeacherInfoModel)
# admin.site.register(EmployeeModel)
# admin.site.register(ManagerModel)


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'designation']


@admin.register(ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city',
                    'designation', 'take_interview', 'hiring']


@admin.register(Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section',
                    'attendence', 'hw']


@admin.register(Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'section',
                    'attendence', 'hw']
