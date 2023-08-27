from django.contrib import admin
from first_app.models import StudentModel, StudentInfoModel, TeacherInfoModel, EmployeeModel, ManagerModel
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
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city',
                    'designation', 'take_interview', 'hiring']
