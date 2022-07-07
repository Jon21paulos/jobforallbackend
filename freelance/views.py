from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from freelance.models import FreelanceJobs
from freelance.serializers import ReadFreelanceJobSerializer,FreelanceJobSerializer
from freelance.pagination import CustomPageNumberPagination
# @permission_classes([IsAuthenticated])
class FreelanceJobList(generics.ListAPIView):
    queryset = FreelanceJobs.objects.all();
    serializer_class = ReadFreelanceJobSerializer
    #permission_classes([IsAuthenticated])
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['Title','Deadline','Jobtime','Jobtype','Salary','City','Description']

    pagination_class = CustomPageNumberPagination



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def FreelanceJobDetail(request, id):
    jobs = FreelanceJobs.objects.get(JobId=id)
    jobs_serializer = FreelanceJobSerializer(jobs, many=False)
    return Response(jobs_serializer.data)

# @permission_classes([IsAuthenticated])
class AddFreelanceJob(generics.GenericAPIView):
    serializer_class = FreelanceJobSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": FreelanceJobSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })


class UpdateFreelanceJob(generics.GenericAPIView):
    serializer_class = FreelanceJobSerializer

    def get_object(self, pk):
        return FreelanceJobs.objects.get(JobId=pk)

    def put(self, request, pk, format=None):
        job_id = self.get_object(pk)
        serializer = FreelanceJobSerializer(job_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                # "message": "job updated successfully"
                "message":serializer.data
            })
        elif serializer.errors():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteFreelanceJob(request, id):
    job = FreelanceJobs.objects.get(JobId=id)
    job.delete()
    return Response("Deleted Successfully")
