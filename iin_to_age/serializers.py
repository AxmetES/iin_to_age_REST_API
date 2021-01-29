import datetime
from datetime import date

from rest_framework import serializers

from iin_to_age.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


