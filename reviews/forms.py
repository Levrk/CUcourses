from django import forms
from .models import review

class ReviewForm(forms.ModelForm):
    """Form layout to create a review"""
    class Meta:
        model = review
        fields = [ 'course', 'instructor', 'reviewText', 'anon']