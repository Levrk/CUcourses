from django import forms
from .models import review

class ReviewForm(forms.ModelForm):
    """Form layout to create a review"""
    course = forms.CharField(label="Course Name")
    instructor = forms.CharField(label="Instructor Name")
    reviewText = forms.CharField(label="Review Text")
    anon = forms.BooleanField(label="Anonymous", required=False)
    textbook = forms.BooleanField(label="Textbook Required", required=False)
    OPTIONS = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    fun = forms.ChoiceField(choices=OPTIONS, widget=forms.CheckboxInput)
    interesting = forms.ChoiceField(choices=OPTIONS, widget=forms.CheckboxInput)
    difficult = forms.ChoiceField(choices=OPTIONS, widget=forms.CheckboxInput)
    
    class Meta:
        model = review
        fields = [ 'course', 'instructor', 'reviewText', 'anon','textbook','fun','interesting','difficult']
        widgets = {
            'anon': forms.TextInput(attrs={'class': 'left-label'}),
            'textbook': forms.TextInput(attrs={'class': 'left-label'})
        }
        #labels = {'course':'CourseCode', 'instructor': 'Professor','reviewText': 'Review', 'anon':'Post Anonymously'}