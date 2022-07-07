from django.db import models
from apply.models import Apply
from account.models import Employer

# Create your models here.
class Candidates(models.Model):
    CandidateId = models.AutoField(primary_key=True)
    # ApplyId = models.ForeignKey(Apply, on_delete=models.CASCADE, null=True, related_name="applyId")
    # EmployerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="empId")

    created_at = models.DateTimeField(auto_now_add=True)
