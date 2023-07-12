from django.db import models
from Home.models import InternshipPrograms


# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=250)
    
    def __str__(self):
        return '{}'.format(self.level)


class Levelperprogram(models.Model):
    c_name = models.ForeignKey(InternshipPrograms, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    desc = models.TextField()
    
    def __str__(self):
        return '{}'.format(str(self.c_name) + str(self.level))


class Contents(models.Model):
    level_per_program = models.ForeignKey(Levelperprogram, on_delete=models.CASCADE)
    content_name = models.CharField(max_length=250)
    contents = models.FileField(upload_to='program_videos/')
    
    def __str__(self):
        return '{}'.format(str(self.level_per_program) + str(self.content_name))
