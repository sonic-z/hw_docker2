from django.contrib import admin
from .models import Sensor, Measurement

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Measurement)
