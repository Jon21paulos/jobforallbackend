from rest_framework import generics,filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from videochat.models import Vchat
from job.pagination import CustomPageNumberPagination
from  videochat.serializers import VchatSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class AddVchat(generics.GenericAPIView):
    serializer_class = VchatSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": VchatSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def VchatDetail(request, pk):
    vchat = Vchat.objects.get(JobseekerId=pk)
    vchat_serializer = VchatSerializer(vchat, many=False)
    # return Response(vchat_serializer.data)
    return Response({
        "data": vchat_serializer.data
    })

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteVchat(request, pk):
    vchat = Vchat.objects.get(JobseekerId=pk)
    vchat.delete()
    return Response("Deleted Successfully")


# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def VchatJ(request):
#     job_data = JSONParser().parse(request)
#     jobs_serializer = JobSerializer(data=job_data)
#     if jobs_serializer.is_valid():
#         jobs_serializer.save()
#         return Response("Added Successfully")
#     return Response("Failed to Add")

# @permission_classes([IsAuthenticated])
#
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def UpdateJob(request, id):
#     job_data = JSONParser().parse(request)
#     # department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
#     job = Jobs.objects.get(JobId=id)
#     jobs_serializer = JobSerializer(job, data=job_data)
#     if jobs_serializer.is_valid():
#         jobs_serializer.save()
#         return Response("Updated Successfully")
#     return Response("Failed to Update")
#
#
