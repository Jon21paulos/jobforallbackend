from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from job.models import Jobs
from job.pagination import CustomPageNumberPagination
from job.serializers import JobSerializer,ReadJobSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# @permission_classes([IsAuthenticated])
class JobList(generics.ListAPIView):
    queryset = Jobs.objects.all();
    serializer_class = ReadJobSerializer
    #permission_classes([IsAuthenticated])
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['Title','Deadline','Jobtime','Jobtype','Salary','City','Description']

    pagination_class = CustomPageNumberPagination


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def JobList(request):
#     jobs = Jobs.objects.all()
#     jobs_serializer = JobSerializer(jobs, many=True)
#     pagination_class = CustomPageNumberPagination
#     return Response(jobs_serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def JobDetail(request, id):
    jobs = Jobs.objects.get(JobId=id)
    jobs_serializer = JobSerializer(jobs, many=False)
    return Response(jobs_serializer.data)


# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def AddJob(request):
#     job_data = JSONParser().parse(request)
#     jobs_serializer = JobSerializer(data=job_data)
#     if jobs_serializer.is_valid():
#         jobs_serializer.save()
#         return Response("Added Successfully")
#     return Response("Failed to Add")

# @permission_classes([IsAuthenticated])
class AddJob(generics.GenericAPIView):
    serializer_class = JobSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": JobSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })


class UpdateJob(generics.GenericAPIView):
    serializer_class = JobSerializer

    def get_object(self, pk):
        return Jobs.objects.get(JobId=pk)

    def put(self, request, pk, format=None):
        job_id = self.get_object(pk)
        serializer = JobSerializer(job_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                # "message": "job updated successfully"
                "message":serializer.data
            })
        elif serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteJob(request, id):
    job = Jobs.objects.get(JobId=id)
    job.delete()
    return Response("Deleted Successfully")

