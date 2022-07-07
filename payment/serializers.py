from rest_framework import serializers
from payment.models import Payment
from account.serializers import EmployerProfileSerializer,JobseekerProfileSerializer
from job.serializers import JobSerializer
class ReadPaymentSerializer(serializers.ModelSerializer):
    freelancerId = JobseekerProfileSerializer(read_only=True)
    employerId = EmployerProfileSerializer(read_only=True)
    jobId = JobSerializer(read_only=True)
    class Meta:
        model=Payment
        fields='__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
