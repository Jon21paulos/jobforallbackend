from telnetlib import STATUS

from account.models import Employer, Jobseeker, User
from .serializers import JobseekerSignupSerializer, EmployerSignupSerializer, UserSerializer, \
    JobseekerProfileSerializer, EmployerProfileSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


class JobseekerSignupView(generics.GenericAPIView):
    serializer_class = JobseekerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })

# @permission_classes([IsAuthenticated])
class UserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        return User.objects.get(id=pk)

    def get(self, request, pk, format=None):
        user_id = self.get_object(pk)
        serializer = UserSerializer(user_id)
        return Response({
            "user": serializer.data
        })



class EmployerSignupView(generics.GenericAPIView):
    serializer_class = EmployerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "account created successfully"
        })


class JobseekerEditProfileView(generics.GenericAPIView):
    serializer_class = JobseekerProfileSerializer

    def get_object(self, pk):
        return Jobseeker.objects.get(user_id=pk)

    def put(self, request, pk, format=None):
        jobeeker_id = self.get_object(pk)
        serializer = JobseekerProfileSerializer(jobeeker_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "profile updated successfully"
            })
        elif serializer.errors():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobseekerProfileView(generics.GenericAPIView):
    serializer_class = JobseekerProfileSerializer

    def get_object(self, pk):
        return Jobseeker.objects.get(user_id=pk)

    def get(self, request, pk, format=None):
        jobeeker_id = self.get_object(pk)
        serializer = JobseekerProfileSerializer(jobeeker_id)
        return Response({
            "user": serializer.data
        })


class EmployerEditProfileView(generics.GenericAPIView):
    serializer_class = EmployerProfileSerializer

    def get_object(self, pk):
        return Employer.objects.get(user_id=pk)

    def put(self, request, pk, format=None):
        employer_id = self.get_object(pk)
        serializer = EmployerProfileSerializer(employer_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "profile updated successfully"
            })
        elif serializer.errors():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerProfileView(generics.GenericAPIView):
    serializer_class = EmployerProfileSerializer

    def get_object(self, pk):
        return Employer.objects.get(user_id=pk)

    def get(self, request, pk, format=None):
        employer_id = self.get_object(pk)
        serializer = EmployerProfileSerializer(employer_id)
        return Response({
            "user": serializer.data
        })
