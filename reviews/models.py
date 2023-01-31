from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    classCode = models.CharField(max_length=10)
    className = models.CharField(max_length=40)
    instructor = models.CharField(max_length=30)
    reviewText = models.TextField(null=False, blank=False)
    anon = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.className