from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from feedback.models import Testimonial,Rating
from feedback.serializers import TestimonialSerializer,RatingSerializer,ReadRatingSerializer,ReadTestimonialSerializer



class TestimonialList(generics.ListAPIView):
    queryset = Testimonial.objects.all();
    serializer_class = ReadTestimonialSerializer
    filterset_fields = '__all__'

    #permission_classes([IsAuthenticated])
    # pagination_class = CustomPageNumberPagination

class AddTestimonial(generics.GenericAPIView):
    serializer_class = TestimonialSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        testi = serializer.save()
        return Response({
            "user": TestimonialSerializer(testi, context=self.get_serializer_context()).data,
            "message": "you sent"
        })

@api_view(['DELETE'])
def DeleteTestimonial(request, id):
    testi = Testimonial.objects.get(testimonialId=id)
    testi.delete()
    return Response("Deleted Successfully")


class RatingList(generics.ListAPIView):
    queryset = Rating.objects.all();
    serializer_class = ReadRatingSerializer
    filterset_fields = '__all__'

    #permission_classes([IsAuthenticated])
    # pagination_class = CustomPageNumberPagination

class AddRating(generics.GenericAPIView):
    serializer_class = RatingSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()
        return Response({
            "user": RatingSerializer(rating, context=self.get_serializer_context()).data,
            "message": "you sent"
        })

@api_view(['DELETE'])
def DeleteRating(request, id):
    rating = Rating.objects.get(ratingId=id)
    rating.delete()
    return Response("Deleted Successfully")

