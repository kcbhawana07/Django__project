from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'booking_date', 'time_slot', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'service__name')
    ordering = ('-booking_date',)
