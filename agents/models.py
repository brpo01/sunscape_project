from django.db import models
from datetime import datetime

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d/')
    description = models.TextField(max_length=400)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name