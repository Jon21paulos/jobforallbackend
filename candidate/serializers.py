from rest_framework import serializers
from candidate.models import Candidates
from apply.serializers import ReadApplySerializer

class ReadCandidateSerializer(serializers.ModelSerializer):
    ApplyId = ReadApplySerializer(read_only=True)
    class Meta:
        model=Candidates
        fields='__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidates
        fields='__all__'
