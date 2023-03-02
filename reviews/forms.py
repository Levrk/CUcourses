from django import forms
from .models import review

class ReviewForm(forms.ModelForm):
    """Form layout to create a review"""
    course = forms.CharField(label="Course Name")
    instructor = forms.CharField(label="Instructor Name")
    reviewText = forms.CharField(label="Review Text")
    anon = forms.BooleanField(label="Anonymous", required=False)
    
    class Meta:
        model = review
        fields = [ 'course', 'instructor', 'reviewText', 'anon']
        widgets = {
            'anon': forms.TextInput(attrs={'class': 'left-label'})
        }
        #labels = {'course':'CourseCode', 'instructor': 'Professor','reviewText': 'Review', 'anon':'Post Anonymously'}