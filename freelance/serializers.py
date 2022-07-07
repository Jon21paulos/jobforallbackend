from rest_framework import serializers
from freelance.models import FreelanceJobs
from account.serializers import EmployerProfileSerializer

class ReadFreelanceJobSerializer(serializers.ModelSerializer):
    user = EmployerProfileSerializer(read_only=True)
    class Meta:
        model=FreelanceJobs
        fields='__all__'

class FreelanceJobSerializer(serializers.ModelSerializer):
    class Meta:
        model=FreelanceJobs
        fields='__all__'
