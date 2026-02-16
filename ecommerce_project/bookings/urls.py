from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>/', views.create_booking, name='create'),
    path('success/', views.success, name='success'),
    path('history/', views.history, name='history'),
    path('cancel/<int:id>/', views.cancel, name='cancel'),

]