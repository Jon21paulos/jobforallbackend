from rest_framework import serializers
from account.models import Jobseeker, User
from apply.models import Apply
from account.serializers import JobseekerProfileSerializer,EmployerProfileSerializer,UserSerializer
from job.serializers import JobSerializer
import django_filters

class FilterApplySerializer(serializers.ModelSerializer):
    ApplierId = JobseekerProfileSerializer(read_only=True)
    EmployerId = EmployerProfileSerializer(read_only=True)
    PostId = JobSerializer(read_only=True)

    class Meta:
        model = Apply
        fields = '__all__'



class ReadApplySerializer(serializers.ModelSerializer):
    ApplierId = JobseekerProfileSerializer(read_only=True)
    EmployerId = EmployerProfileSerializer(read_only=True)
    PostId = JobSerializer(read_only=True)

    class Meta:
        model = Apply
        fields = '__all__'


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'
