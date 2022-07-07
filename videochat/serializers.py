from rest_framework import serializers
from videochat.models import Vchat

class VchatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vchat
        fields='__all__'


