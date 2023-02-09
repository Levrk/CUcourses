
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import review, course
# Create your views here.

class allReviews(ListView):
    model = review
    context_object_name = "reviews"
    template_name = "reviews/allReviews.html"

class searchReviews(ListView):
    model = review
    context_object_name = "reviews"
    template_name = "reviews/searchReviews.html"

    def get_context_data(self, *args, **kwargs):
        # getting context variables so search terms can be referenced in searchReviews template
        context = super().get_context_data(*args, **kwargs)
        context['course_code'] = self.request.GET.get('course_code').upper().replace(" ","")
        return context

    def get_queryset(self):
        #gets the desired course code from the form in searchReviews
        course_code = self.request.GET.get('course_code').upper().replace(" ","")
        #locating the correct model attribute and generating query set
        courses = course.objects.filter(courseCode=course_code)
        queryset = review.objects.filter(course__in=courses)
        return queryset
#select * from reviews_review;
#WHERE course_id IN (SELECT id from reviews_course WHERE courseCode = "CSCI121");

class reviewDetails(DetailView):
    model = review
    context_object_name = "review"
    template_name = "reviews/reviewDetails.html"

class createReview(CreateView):
    model = review
    fields = '__all__'
    ##below is where we send the user after succesfully submitting form
    success_url = reverse_lazy('reviews')