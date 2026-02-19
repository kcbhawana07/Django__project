from django.contrib import admin
from .models import Service, ServiceCategory
# Register your models here.

admin.site.register(ServiceCategory)
admin.site.register(Service)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)


admin.site.register(ServiceCategory)