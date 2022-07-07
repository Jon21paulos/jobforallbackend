from django.db import models
from django.conf import settings
from account.models import Employer
User = settings.AUTH_USER_MODEL
# Create your models here.
class FreelanceJobs(models.Model):
    user = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    JobId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Deadline = models.CharField(max_length=500)
    Jobtime = models.CharField(max_length=500)
    Jobtype = models.CharField(max_length=500)
    Salary = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Title
