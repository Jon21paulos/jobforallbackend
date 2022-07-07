from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_serviceseeker = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Jobseeker(models.Model):
    user = models.OneToOneField(User, related_name="jobseeker", on_delete=models.CASCADE)
    JobseekerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    adderss = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.TextField(null=True, blank=True)
    degree = models.CharField(max_length=20, null=True, blank=True)
    grade = models.CharField(max_length=20, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    tempo = models.TextField(null=True, blank=True)
    company_name = models.CharField(max_length=20, null=True, blank=True)
    job_title = models.CharField(max_length=20, null=True, blank=True)
    start_and_end_date = models.CharField(max_length=20, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    project_title = models.CharField(max_length=20, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    achivement_and_award = models.TextField(null=True, blank=True)
    activities = models.TextField(null=True,blank=True)
    social_media = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    # def __int__(self):
    #     return self.user


class Employer(models.Model):
    user = models.OneToOneField(User, related_name="employer", on_delete=models.CASCADE)
    EmployerId = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    adderss = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=20, null=True, blank=True)
    objective = models.TextField(null=True, blank=True)
    achivement_and_award = models.TextField(null=True, blank=True)
    activities = models.TextField(null=True,blank=True)
    social_media = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class ServiceSeeker(models.Model):
    user = models.OneToOneField(User, related_name="serviceseeker", on_delete=models.CASCADE)
    ServiceSeekerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    adderss = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
