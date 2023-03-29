from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class department(models.Model):
    """
    (A model for storing department data)

    deptCode -> 'CSCI' or 'PHIL'
    deptName -> 'Computer Science' or 'Philosophy'
    """
    deptCode = models.CharField(max_length=10)
    deptName = models.CharField(max_length=40)

    def __str__(self):
        return self.deptName

class course(models.Model):
    """
    (A model for storing course data)

    courseCode -> 'CSCI121' or 'PHIL124'
    courseName -> 'Introduction to Computing' or 'Philosophy of Death'
    dept -> Instance of the [department] model
    """
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=40)
    dept = models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.courseCode
    
class review(models.Model):
    """
    (A model for storing course reviews)

    user -> Instance of the [User] model
    course -> Instance of the [course] model
    instructor -> str : Teacher fname & lname
    reviewText -> str : The review itself
    anon -> bool : Does the user want their name displayed
    created -> Date & time of submission
    good - > needswork
    fun - > needswork
    """
    #nulls should be false in production
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="Anonymous")
    course = models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    instructor = models.CharField(max_length=30)
    reviewText = models.TextField(max_length=800, null=False)
    anon = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    textbook = models.BooleanField(default=True)
    
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    fun = models.CharField(max_length=1, choices=CHOICES,default='3')
    interesting = models.CharField(max_length=1, choices=CHOICES,default='3')
    difficult = models.CharField(max_length=1, choices=CHOICES,default='3')


    def __str__(self):
        return str(self.course)

    def snippet (self):
        """ returns first 150 characters of [reviewText] """
        return "\"" + self.reviewText[:150] + "...\""
    
    class Meta:
        ordering = ['created']