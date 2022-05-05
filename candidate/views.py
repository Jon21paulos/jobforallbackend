from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from candidate.models import Candidates
from candidate.serializers import ReadCandidateSerializer,CandidateSerializer
from rest_framework.response import Response


class CandidateList(ListCreateAPIView):
    queryset = Candidates.objects.all()
    serializer_class = ReadCandidateSerializer
    filterset_fields = '__all__'

class AddCandidate(generics.GenericAPIView):
    serializer_class = CandidateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": CandidateSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you applied"
        })

