# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from .serializers import MeasurementSerializer, SensorSerializer, SensorSerializerEasy


class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializerEasy


class ChangeSensorData(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasure(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class GetListSensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class GetSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
