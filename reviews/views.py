from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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