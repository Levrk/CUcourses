from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import review
# Create your views here.

class allReviews(ListView):
    model = review
    context_object_name = "reviews"
    template_name = "reviews/allReviews.html"

class reviewDetails(DetailView):
    model = review
    context_object_name = "review"
    template_name = "reviews/reviewDetails.html"

class createReview(CreateView):
    model = review
    fields = '__all__'
    ##below is where we send the user after succesfully submitting form
    success_url = reverse_lazy('reviews')