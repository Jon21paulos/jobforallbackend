from rest_framework import serializers
from job.models import Jobs
from account.serializers import EmployerProfileSerializer

class ReadJobSerializer(serializers.ModelSerializer):
    user = EmployerProfileSerializer(read_only=True)
    class Meta:
        model=Jobs
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields='__all__'
