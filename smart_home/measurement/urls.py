from django.urls import path
from .views import CreateMeasurementView, LCSensorsView, RUSensorsView

urlpatterns = [
    path('sensors/<pk>/', LCSensorsView.as_view()),
    path('sensors/', LCSensorsView.as_view()),
    path('sensors/update/<pk>/', RUSensorsView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
]
