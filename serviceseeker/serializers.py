from rest_framework import serializers
from serviceseeker.models import ServiceSeeker,RequestService
from account.serializers import JobseekerProfileSerializer,ServiceSeekerProfileSerializer

class ReadServiceSeekerSerializer(serializers.ModelSerializer):
    user = JobseekerProfileSerializer(read_only=True)
    class Meta:
        model=ServiceSeeker
        fields='__all__'

class ServiceSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceSeeker
        fields='__all__'


class ReadRequestServiceSerializer(serializers.ModelSerializer):
    jobseekerServiceId = JobseekerProfileSerializer(read_only=True)
    ServiceSeekerUserId = ServiceSeekerProfileSerializer(read_only=True)
    ServiceSeekerId = ServiceSeekerSerializer(read_only=True)

    class Meta:
        model = RequestService
        fields = '__all__'


class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestService
        fields = '__all__'
