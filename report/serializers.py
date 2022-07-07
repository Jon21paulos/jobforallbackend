from rest_framework import serializers
from report.models import Report,Warning,Notify
from account.serializers import UserSerializer,EmployerProfileSerializer,JobseekerProfileSerializer

class ReadReportSerializer(serializers.ModelSerializer):
    reporter = UserSerializer(read_only=True)
    reported = UserSerializer(read_only=True)

    class Meta:
        model=Report
        fields='__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields='__all__'

class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Warning
        fields='__all__'



class ReadNotifySerializer(serializers.ModelSerializer):
    notified = JobseekerProfileSerializer(read_only=True)
    notifier = EmployerProfileSerializer(read_only=True)

    class Meta:
        model= Notify
        fields='__all__'

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model=Notify
        fields='__all__'
