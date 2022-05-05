from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from apply.models import Apply
from apply.serializers import ReadApplySerializer, ApplySerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from job.pagination import CustomPageNumberPagination

class ApplyList(ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ReadApplySerializer
    filterset_fields = '__all__'


class AddApplier(generics.GenericAPIView):
    serializer_class = ApplySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": ApplySerializer(apply, context=self.get_serializer_context()).data,
            "message": "you applied"
        })

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteApply(request, id):
    apply = Apply.objects.get(ApplyId=id)
    apply.delete()
    return Response("Deleted Successfully")

# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def AddApplier(request):
#     apply_data = JSONParser().parse(request)
#     apply_serializer = ApplySerializer(data=apply_data)
#     if apply_serializer.is_valid():
#         apply_serializer.save()
#         return Response("Added Successfully")
#     return Response("Failed to Add")

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def JobList(request):
#     jobs = Jobs.objects.all()
#     jobs_serializer = JobSerializer(jobs, many=True)
#     pagination_class = CustomPageNumberPagination
#     return Response(jobs_serializer.data)

#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def ApplierDetail(request, id):
#     apply = Apply.objects.get(JobId=id)
#     jobs_serializer = ApplySerializer(apply, many=False)
#     return Response(jobs_serializer.data)
#
#

#
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
