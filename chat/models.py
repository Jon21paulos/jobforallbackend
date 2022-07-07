from django.db import models
from django.conf import settings
from account.models import Jobseeker,Employer
from job.models import Jobs
User = settings.AUTH_USER_MODEL
# Create your models here.
class Chat(models.Model):
    ChatId = models.AutoField(primary_key=True)
    JobseekerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jobseekerId")
    EmployerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="employeId")
    JobId = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True, related_name="jid")
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def __int__(self):
        return self.ChatId

class Message(models.Model):
    MessageId = models.AutoField(primary_key=True)
    ChatId = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, related_name="chatId")
    Message = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="sender")
    created_at = models.DateTimeField(auto_now_add=True)
