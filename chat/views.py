from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat
from chat.serializers import ReadChatSerializer,ChatSerializer
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
