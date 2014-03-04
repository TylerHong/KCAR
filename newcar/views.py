#-*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from newcar.models import Maker, Car
from newcar.serializers import MakerSerializer, CarSerializer

class CarList(APIView):
  def get(self, request, mcode='aa', ccode='ANY', format=None):
    # 아무 조건도 없다면 메이커 명을 리턴
    if (mcode == 'aa'):
      makers = Maker.objects.all()
      serializer = MakerSerializer(makers, many=True)
      return Response(serializer.data)
    # 메이커명이 주어졌다면 자동차명을 리턴
    elif (mcode <> 'aa' and ccode == 'ANY'):
      maker = Maker.objects.filter(mcode=mcode)
      cars = Car.objects.filter(mid=maker)
      serializer = CarSerializer(cars, many=True)
      return Response(serializer.data)
    # 메이커명과 자동차명이 주어졌다면 사양을 리턴
    elif (mcode <> 'aa' and ccode <> 'ANY'):
      maker = Maker.objects.filter(mcode=mcode)
      cars = Car.objects.filter(mid=maker, ccode=ccode)
      serializer = CarSerializer(cars, many=True)
      return Response(serializer.data)
