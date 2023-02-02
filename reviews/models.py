from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class department(models.Model):
    deptCode = models.CharField(max_length=10)
    deptName = models.CharField(max_length=40)

    def __str__(self):
        return self.deptName

class course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=40)
    dept = models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.courseName
    
class review(models.Model):
    #nulls should be false in production
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="Anonymous")
    course = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    instructor = models.CharField(max_length=30)
    reviewText = models.TextField(max_length=800, null=False)
    anon = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.course)
    
    class Meta:
        ordering = ['created']