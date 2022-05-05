from curses import meta
from rest_framework import serializers
from .models import User, Employer, Jobseeker




class JobseekerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_jobseeker = True
        user.save()
        Jobseeker.objects.create(user=user)
        return user



class EmployerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_employer = True
        user.save()
        Employer.objects.create(user=user)
        return user

class JobseekerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobseeker
        fields = '__all__'
        # fields = ['user','name','adderss','phone','profile_photo','degree','grade','year','tempo','company_name','job_title','start_and_end_date','detail','skills','objective','project_title','project_description','achivement_and_award','activities','social_media']

class UserSerializer(serializers.ModelSerializer):
    # id = JobseekerProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

        # fields = ['id','username', 'email','is_employer']


class EmployerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

        # fields = ['user','company_name','adderss','phone','profile_photo','description','website','objective','achivement_and_award','activities','social_media']
       
