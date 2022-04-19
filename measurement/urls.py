from django.urls import path
from .views import CreateSensor, ChangeSensorData, CreateMeasure, GetListSensors, GetSensor

urlpatterns = [
    path('sensors/', CreateSensor.as_view()),
    path('sensors/<pk>/', ChangeSensorData.as_view()),
    path('measurements/', CreateMeasure.as_view()),
    path('get_list_sensors/', GetListSensors.as_view()),
    path('get_sensor/<pk>/', GetSensor.as_view())
]
