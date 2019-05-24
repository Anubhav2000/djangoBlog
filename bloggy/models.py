from django.db import models as Models
from django.conf import settings
from django.utils import timezone

class post(Models.Model):
    id = Models.AutoField(primary_key=True)
    author = Models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=Models.CASCADE)
    title = Models.CharField(max_length=100)
    text = Models.TextField()
    createdDate = Models.DateTimeField(auto_now=True)
    publishedDate = Models.DateTimeField(auto_now=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()
    
    def _str_(self):
        return self.title
    

# Create your models here.
