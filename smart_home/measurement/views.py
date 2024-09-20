# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Sensor
from .serializers import SensorDetailSerializer, AddMeasurementSerializer, SensorSerializer


class CreateMeasurementView(CreateAPIView):
    serializer_class = AddMeasurementSerializer


class LCSensorsView(ListCreateAPIView): #Создание и вывод списка сенсоров
    is_list = True
    serializer_class = SensorSerializer

    def get_queryset(self):
        if 'pk' in str(self.kwargs):
            self.is_list = False
            return Sensor.objects.filter(id=self.kwargs['pk'])
        else:
            return Sensor.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        if self.is_list:
            serializer = SensorSerializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        else:
            serializer = SensorDetailSerializer(self.get_queryset(), many=False)
            return Response(serializer.data)


class RUSensorsView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        if 'pk' in str(self.kwargs):
            return Sensor.objects.filter(id=self.kwargs['pk'])
        else:
            return Sensor.objects.all().order_by('id')


