
from django.db import models
from django.conf import settings
from account.models import Jobseeker
User = settings.AUTH_USER_MODEL

# Create your models here.
class Vchat(models.Model):
    JobseekerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jsId")
    VchatId = models.TextField(null=True, blank=True)


