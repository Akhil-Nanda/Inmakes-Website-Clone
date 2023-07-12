from django.db import models


# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=250)
    
    def __str__(self):
        return '{}'.format(self.language)


class InternshipPrograms(models.Model):
    name = models.CharField(max_length=250, blank=False)
    image = models.ImageField(upload_to='images')
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.name)

