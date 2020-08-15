from rest_framework import serializers

from .models import OfficeModel


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'
