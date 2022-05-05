from rest_framework import generics,filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404

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

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateJob(request, id):
    job_data = JSONParser().parse(request)
    # department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
    job = Jobs.objects.get(JobId=id)
    jobs_serializer = JobSerializer(job, data=job_data)
    if jobs_serializer.is_valid():
        jobs_serializer.save()
        return Response("Updated Successfully")
    return Response("Failed to Update")


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteJob(request, id):
    job = Jobs.objects.get(JobId=id)
    job.delete()
    return Response("Deleted Successfully")
