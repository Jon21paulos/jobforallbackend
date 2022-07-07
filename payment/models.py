
from django.db import models
from django.conf import settings
from account.models import Jobseeker,Employer
from job.models import Jobs
from chat.models import Chat

# Create your models here.
class Payment(models.Model):
    PaymentId = models.AutoField(primary_key=True)
    freelancerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="fi")
    employerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="ei")
    jobId = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True, related_name="ji")
    chatId = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, related_name="ci")
    payment = models.IntegerField()
    is_fullpayment = models.BooleanField(default=False)
