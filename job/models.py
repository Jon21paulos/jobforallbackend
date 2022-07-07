from django.db import models
from django.conf import settings
from account.models import Employer
User = settings.AUTH_USER_MODEL
# Create your models here.
class Jobs(models.Model):
    user = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    JobId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=500)
    Deadline = models.DateTimeField()
    Jobtype = models.CharField(max_length=500)
    Salary = models.IntegerField()
    City = models.CharField(max_length=500)
    Description = models.TextField()
    is_freelancer = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)


    def __str__(self):
        return self.Title
