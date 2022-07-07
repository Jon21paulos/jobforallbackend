from django.db import models
from django.conf import settings
from account.models import Jobseeker,Employer
# Create your models here.
class Testimonial(models.Model):
    testimonialId = models.AutoField(primary_key=True)
    jobseekerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jbsId")
    employerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="eId")
    testimonial = models.TextField(null=True, blank=True)


class Rating(models.Model):
    ratingId = models.AutoField(primary_key=True)
    jobseekerId = models.ForeignKey(Jobseeker, on_delete=models.CASCADE, null=True, related_name="jbId")
    employerId = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True, related_name="erId")
    rating = models.IntegerField(null=True, blank=True)

