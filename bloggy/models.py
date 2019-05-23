from django.db import models as Models
from django.conf import settings
from django.utils import timezone

class post(Models.Model):
    author = Models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=Models.CASCADE)
    title = Models.CharField(max_length=100)
    text = Models.TextField()
    createdDate = Models.DateTimeField()
    publishedDate = Models.DateTimeField()

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    
    def _str_(self):
        return self.title
    

# Create your models here.
