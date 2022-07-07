from rest_framework import serializers
from account.serializers import JobseekerProfileSerializer, EmployerProfileSerializer
from feedback.models import Testimonial,Rating

class ReadTestimonialSerializer(serializers.ModelSerializer):
    employerId = EmployerProfileSerializer(read_only=True)

    class Meta:
        model = Testimonial
        fields = '__all__'

class ReadRatingSerializer(serializers.ModelSerializer):
    employerId = EmployerProfileSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
