from rest_framework import serializers
from .models import Data, Record


class DataSerializer(serializers.ModelSerializer):
    device = serializers.CharField(write_only=True)
    unit = serializers.SerializerMethodField()

    class Meta:
        model = Data
        fields = ['device', 'unit', 'value', 'datetime']

    def get_unit(self, obj):
        return obj.get_unit_display()


class RecordSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True)
    devices = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Record
        fields = ['id', 'record_time', 'data', 'devices']

    def create(self, validated_data):
        data = validated_data.pop('data')
        devices = validated_data.pop('devices')
        record = Record.objects.create(**validated_data)
        for dt in data:
            dt['unit'] = devices[dt['device']]
            Data.objects.create(record=record, **dt)
        return record
