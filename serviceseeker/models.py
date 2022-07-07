from django.db import models
from django.conf import settings
from account.models import Employer,Jobseeker,ServiceSeeker as ServiceSeekerUser
User = settings.AUTH_USER_MODEL
# Create your models here.



class ServiceSeeker(models.Model):
    user = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True)
    ServiceId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Jobtype = models.CharField(max_length=500)
    service_photo = models.TextField(null=True)
    Salary = models.IntegerField(null=True)
    City = models.CharField(max_length=500)
    Description = models.TextField(null=True)
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return self.Title

class RequestService(models.Model):
    RequestServiceId = models.AutoField(primary_key=True)
    jobseekerServiceId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jobseekerServiceId")
    ServiceSeekerUserId = models.ForeignKey(ServiceSeekerUser, on_delete=models.CASCADE, null=True, related_name="ServiceSeekerUserId")
    ServiceSeekerId = models.ForeignKey(ServiceSeeker, on_delete=models.CASCADE, null=True, related_name="ServiceSeekerId")
    created_at = models.DateTimeField(auto_now_add=True)
