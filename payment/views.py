from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from payment.models import Payment
from payment.serializers import PaymentSerializer,ReadPaymentSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def payment(request):
    obj = {
        "process": "Express",
        "merchantOrderId": "l710.0",
        "merchantId": "SB1617",
        "ipnUrl": "",
        "successUrl": "http://localhost:3000/home/employer/chat/verification/success",
        "cancelUrl": "http://localhost:3000/home/employer/chat/verification/cancel",
        "itemId": 60,
        "itemName": "Billing",
        "unitPrice": 0.0,
        "quantity": 1,

    }
    return Response(
        {'obj':obj}
    )

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all();
    serializer_class = ReadPaymentSerializer
    #permission_classes([IsAuthenticated])
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = '__all__'


class AddPayment(generics.GenericAPIView):
    serializer_class = PaymentSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": PaymentSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you posted"
        })


class UpdatePayment(generics.GenericAPIView):
    serializer_class = PaymentSerializer

    def get_object(self, pk):
        return Payment.objects.get(PaymentId=pk)

    def put(self, request, pk, format=None):
        p_id = self.get_object(pk)
        serializer = PaymentSerializer(p_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                # "message": "job updated successfully"
                "message":serializer.data
            })
        elif serializer.errors:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def DeletePayment(request, id):
    p = Payment.objects.get(PaymentId=id)
    p.delete()
    return Response("Deleted Successfully")

