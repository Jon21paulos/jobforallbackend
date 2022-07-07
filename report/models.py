from django.db import models
from django.conf import settings
from account.models import Jobseeker,Employer
User = settings.AUTH_USER_MODEL
# Create your models here.

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="reporter")
    reported = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="reported")
    reportId = models.AutoField(primary_key=True)
    ReportMessage = models.CharField(max_length=500)

class Warning(models.Model):
    warningId = models.AutoField(primary_key=True)
    warnedUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="warnedUser")
    warningMessage = models.CharField(max_length=500)

class Notify(models.Model):
    NotifyId = models.AutoField(primary_key=True)
    notifier = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="empNot")
    notified = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jobNot")
    notify = models.CharField(max_length=500)

