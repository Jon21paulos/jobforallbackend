from django.db import models
from django.conf import settings
from job.models import Jobs
from account.models import Jobseeker,Employer

User = settings.AUTH_USER_MODEL
# Create your models here.
class Apply(models.Model):
    ApplyId = models.AutoField(primary_key=True)
    EmployerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="employerId")
    ApplierId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="applierId")
    PostId = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

