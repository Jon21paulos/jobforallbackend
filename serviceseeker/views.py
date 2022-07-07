from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from serviceseeker.models import ServiceSeeker,RequestService
from serviceseeker.pagination import CustomPageNumberPagination
from serviceseeker.serializers import ServiceSeekerSerializer,ReadServiceSeekerSerializer,ReadRequestServiceSerializer,RequestServiceSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# @permission_classes([IsAuthenticated])

class ServiceSeekerList(generics.ListAPIView):
    queryset = ServiceSeeker.objects.all();
    serializer_class = ReadServiceSeekerSerializer
    #permission_classes([IsAuthenticated])
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['Title','Deadline','Jobtime','Jobtype','Salary','City','Description']
    pagination_class = CustomPageNumberPagination


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ServiceSeekerDetail(request, id):
    jobs = ServiceSeeker.objects.get(ServiceSeekerId=id)
    jobs_serializer = ServiceSeekerSerializer(jobs, many=False)
    return Response(jobs_serializer.data)


class AddServiceSeeker(generics.GenericAPIView):
    serializer_class = ServiceSeekerSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": ServiceSeekerSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })


class UpdateServiceSeeker(generics.GenericAPIView):
    serializer_class = ServiceSeekerSerializer

    def get_object(self, pk):
        return ServiceSeeker.objects.get(ServiceSeekerId=pk)

    def put(self, request, pk, format=None):
        job_id = self.get_object(pk)
        serializer = ServiceSeekerSerializer(job_id, data=request.data)
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
def DeleteServiceSeeker(request, id):
    job = ServiceSeeker.objects.get(ServiceSeekerId=id)
    job.delete()
    return Response("Deleted Successfully")



class RequestServiceSeekerList(generics.ListAPIView):
    queryset = RequestService.objects.all();
    serializer_class = ReadRequestServiceSerializer
    #permission_classes([IsAuthenticated])
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = '__all__'
    pagination_class = CustomPageNumberPagination


class AddRequestServiceSeeker(generics.GenericAPIView):
    serializer_class = RequestServiceSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": RequestServiceSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })


@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def DeleteRequestServiceSeeker(request, id):
    job = RequestService.objects.get(RequestServiceId=id)
    job.delete()
    return Response("Deleted Successfully")

