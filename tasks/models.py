from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=30,null=False, blank=False)

    description = models.TextField(blank=True)

    
