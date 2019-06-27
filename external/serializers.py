from rest_framework import serializers
from rest_framework.serializers import api_settings, ValidationError
from datetime import datetime


class ExternalBookSerializer(serializers.Serializer):
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(child=serializers.CharField())
    number_of_pages = serializers.IntegerField()
    publisher = serializers.CharField()
    country = serializers.CharField()
    release_date = serializers.DateField()

    def to_internal_value(self, data):
        for key in ['numberOfPages', 'released']:
            if key not in data:
                raise ValidationError({f"{key} field is required"}, code='required')

        data['number_of_pages'] = data.pop('numberOfPages')
        data['release_date'] = datetime.strptime(data.pop('released'), "%Y-%m-%dT%H:%M:%S").date()

        return super().to_internal_value(data)
