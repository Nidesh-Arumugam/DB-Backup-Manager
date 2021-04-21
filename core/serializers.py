from rest_framework import serializers
from .models import databases

class DataSeriallizer(serializers.ModelSerializer):
    class Meta:
        model= databases
        fields=(
            'DBname',
            'IP',
            'Port',
            'UserName',
            'Password'
        )