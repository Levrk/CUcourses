
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import review, course
import re
# Create your views here.

class allReviews(ListView):
    """
    Displays a list of all reviews
    
    Context variable in template -> "reviews"
    Template file -> "reviews/allReviews.html"
    """
    model = review
    context_object_name = "reviews"
    template_name = "reviews/allReviews.html"


class searchReviews(ListView):
    """
    Displays a list of reviews based on query
    
    Context variable in template -> "reviews" 
    Template file -> "reviews/searchReviews.html"
    """
    model = review
    context_object_name = "reviews"
    template_name = "reviews/searchReviews.html"

    def get_context_data(self, *args, **kwargs):
        # getting context variables so search terms can be referenced in searchReviews template
        context = super().get_context_data(*args, **kwargs)
        context['course_code'] = self.request.GET.get('course_code').upper()
        return context

    def get_queryset(self):
        #gets the desired course code from the form in searchReviews
        #adds space between dept and course num if there isn't one
        course_code = re.sub(r'(?<=[a-zA-Z])(?=\d)', ' ', self.request.GET.get('course_code').upper()).strip()
        print(course_code)
        #locating the correct model attribute and generating query set
        courses = course.objects.filter(courseCode=course_code)
        queryset = review.objects.filter(course__in=courses)
        return queryset


class reviewDetails(DetailView):
    """
    Displays details of a single review
    
    Context variable in template -> "review" 
    Template file -> "reviews/reviewDetails.html"
    """
    model = review
    context_object_name = "review"
    template_name = "reviews/reviewDetails.html"

class createReview(CreateView):
    """
    Displays a form for submitting a new review
    
    Context variable in template -> "review" 
    Template file -> "reviews/Review_form.html"
    """
    context_object_name = "review"
    model = review
    fields = '__all__'
    ##below is where we send the user after successfully submitting form
    success_url = reverse_lazy('reviews')
    