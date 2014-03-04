from rest_framework import serializers
from newcar.models import Maker
from newcar.models import Car

class MakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Maker
    fields = ('mid', 'mcode', 'mname')

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('cid', 'mid', 'ccode', 'cname', 'trim')
