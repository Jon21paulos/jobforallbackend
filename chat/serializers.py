from rest_framework import serializers
from chat.models import Chat,Message
from account.serializers import JobseekerProfileSerializer, EmployerProfileSerializer
from job.serializers import JobSerializer


class ReadChatSerializer(serializers.ModelSerializer):
    JobseekerId = JobseekerProfileSerializer(read_only=True)
    EmployerId = EmployerProfileSerializer(read_only=True)
    JobId = JobSerializer(read_only=True)
    class Meta:
        model = Chat
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
