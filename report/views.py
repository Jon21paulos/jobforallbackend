from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from report.models import Report,Warning,Notify
from report.serializers import ReadReportSerializer,ReportSerializer,WarningSerializer,ReadNotifySerializer,NotifySerializer
from report.pagination import CustomPageNumberPagination

# @permission_classes([IsAuthenticated])
class ReportList(generics.ListAPIView):
    queryset = Report.objects.all();
    serializer_class = ReadReportSerializer
    filterset_fields = '__all__'
    #permission_classes([IsAuthenticated])
    pagination_class = CustomPageNumberPagination

class CreateReport(generics.GenericAPIView):
    serializer_class = ReportSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = serializer.save()
        return Response({
            "user": ReportSerializer(report, context=self.get_serializer_context()).data,
            "message": "you sent"
        })


@api_view(['DELETE'])
def DeleteReport(request, id):
    report = Report.objects.get(reportId=id)
    report.delete()
    return Response("Deleted Successfully")



# @permission_classes([IsAuthenticated])
class WarningList(generics.ListAPIView):
    queryset = Warning.objects.all();
    serializer_class = WarningSerializer
    filterset_fields = '__all__'
    #permission_classes([IsAuthenticated])

class CreateWarning(generics.GenericAPIView):
    serializer_class = WarningSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = serializer.save()
        return Response({
            "user": WarningSerializer(report, context=self.get_serializer_context()).data,
            "message": "you sent"
        })


# @permission_classes([IsAuthenticated])
class NotifyList(generics.ListAPIView):
    queryset = Notify.objects.all();
    serializer_class = ReadNotifySerializer
    filterset_fields = '__all__'
    #permission_classes([IsAuthenticated])

class CreateNotify(generics.GenericAPIView):
    serializer_class = NotifySerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = serializer.save()
        return Response({
            "user": NotifySerializer(report, context=self.get_serializer_context()).data,
            "message": "you sent"
        })
