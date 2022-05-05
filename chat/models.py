from django.db import models
from django.conf import settings
from account.models import Jobseeker,Employer

User = settings.AUTH_USER_MODEL
# Create your models here.
class Chat(models.Model):
    ChatId = models.AutoField(primary_key=True)
    JobseekerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jobseekerId")
    EmployerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="employeId")
    Message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


