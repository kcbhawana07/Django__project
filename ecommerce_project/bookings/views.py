from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from services.models import Service
from .models import Booking
from .forms import BookingForm


# Create your views here.
@login_required
def create_booking(request, id):
    service = get_object_or_404(Service, id=id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.service = service
                booking.save()
                return redirect('success')
            except IntegrityError:
                form.add_error(None, "Slot already booked")
    else:
        form = BookingForm()

    return render(request, 'bookings/create.html', {
        'form': form,
        'service': service
    })


@login_required
def success(request):
    return render(request, 'bookings/success.html')


@login_required
def history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/history.html', {
        'bookings': bookings
    })


@login_required
def cancel(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    return redirect('history')



@login_required
def history(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/history.html', {
        'bookings': bookings
    })

