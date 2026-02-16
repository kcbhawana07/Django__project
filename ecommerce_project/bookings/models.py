from django.db import models
from django.contrib.auth.models import User
from services.models import Service
# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    booking_date = models.DateField()
    time_slot = models.TimeField()

    status = models.CharField(max_length=20, default='Confirmed')

    class Meta:
        unique_together = ('service', 'booking_date', 'time_slot')

    def __str__(self):
        return self.service.name
