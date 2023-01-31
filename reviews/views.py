from django.shortcuts import render
from django.views.generic.list import ListView
from .models import review
# Create your views here.

class reviewList(ListView):
    model = review
    context_object_name = "reviews"