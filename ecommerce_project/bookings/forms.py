from django import forms
from .models import Booking
from datetime import date, time


TIME_SLOTS = [
    (time(9, 0), "09:00 AM"),
    (time(11, 0), "11:00 AM"),
    (time(1, 0), "01:00 PM"),
    (time(3, 0), "03:00 PM"),
    (time(5, 0), "05:00 PM"),
]


class BookingForm(forms.ModelForm):
    time_slot = forms.ChoiceField(choices=TIME_SLOTS)

    class Meta:
        model = Booking
        fields = ['booking_date', 'time_slot']

    def clean_booking_date(self):
        d = self.cleaned_data['booking_date']
        if d < date.today():
            raise forms.ValidationError("Past date not allowed")
        return d
