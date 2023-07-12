from django.contrib.auth.models import User
from django.db import models
from Home.models import InternshipPrograms


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    place = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    program = models.ForeignKey(InternshipPrograms, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.user.first_name)

