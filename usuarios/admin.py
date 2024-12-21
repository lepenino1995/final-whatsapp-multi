from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'area', 'jefe')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'area', 'jefe')}),
    )
    list_display = ('username', 'role', 'area', 'jefe', 'is_staff')
    list_filter = ('role', 'area')
    search_fields = ('username', 'email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'superempleado':
            return qs.filter(area=request.user.area)
        return qs

admin.site.register(User, UserAdmin)
