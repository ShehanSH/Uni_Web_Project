
# Register your models here.
# admin.site.register(User)

from django.contrib import admin
from .models import CustomUser, Role
from .models import Faculty, Department

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    list_filter = ('role',)
    search_fields = ('username',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name',)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'faculty_name',)

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department)
admin.site.site_header = 'UOK SPORTS ITEMS & GROUND BOOKING SYSTEM'


