from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat,Message
from chat.serializers import ReadChatSerializer,ChatSerializer,MessageSerializer
# @permission_classes([IsAuthenticated])
class ChatList(generics.ListAPIView):
    queryset = Chat.objects.all();
    serializer_class = ReadChatSerializer
    filterset_fields = '__all__'

    #permission_classes([IsAuthenticated])
    # pagination_class = CustomPageNumberPagination

class AddChat(generics.GenericAPIView):
    serializer_class = ChatSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": ChatSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you sent"
        })

@api_view(['DELETE'])

def DeleteChat(request, id):
    chat = Chat.objects.get(ChatId=id)
    chat.delete()
    return Response("Deleted Successfully")


class MessageList(generics.ListAPIView):
    queryset = Message.objects.all();
    serializer_class = MessageSerializer
    filterset_fields = '__all__'

    #permission_classes([IsAuthenticated])
    # pagination_class = CustomPageNumberPagination

class AddMessage(generics.GenericAPIView):
    serializer_class = MessageSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply = serializer.save()
        return Response({
            "user": MessageSerializer(apply, context=self.get_serializer_context()).data,
            "message": "you sent"
        })

@api_view(['DELETE'])
def DeleteMessage(request, id):
    chat = Chat.objects.get(MessageId=id)
    chat.delete()
    return Response("Deleted Successfully")

class EditChat(generics.GenericAPIView):
    serializer_class = ChatSerializer

    def get_object(self, pk):
        return Chat.objects.get(ChatId=pk)

    def put(self, request, pk, format=None):
        job_id = self.get_object(pk)
        serializer = ChatSerializer(job_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                # "message": "job updated successfully"
                "message":serializer.data
            })
        elif serializer.errors:
            return Response(serializer.errors)

