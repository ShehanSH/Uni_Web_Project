
# Register your models here.
# admin.site.register(User)

from django.contrib import admin
from .models import User, Role
from .models import Faculty, Department

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    list_filter = ('role',)
    search_fields = ('username',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Faculty)
admin.site.register(Department)

