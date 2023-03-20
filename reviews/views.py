
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import review, course, department
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm

"""Import for log in page"""
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import re
# Create your views here.

class CustomLoginView(LoginView):
    """
        Creates log in page using default django login
    """
    template_name =  "reviews/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('reviews')
    
class RegisterPage(FormView):
    """
        Creates the register page using a default django form
        
        blocks registered and logged in users from accessing this page
        
    """
    template_name = 'reviews/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('reviews')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user) 
        return super(RegisterPage, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please try again.')
        return redirect('register')  
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('reviews')
        return super(RegisterPage, self).get(*args, **kwargs)
            
    
    
    

class allReviews(ListView):
    """
    Displays a list of all reviews
    
    Context variable in template -> "reviews"
    Template file -> "reviews/allReviews.html"
    """
    model = review
    context_object_name = "reviews"
    template_name = "reviews/allReviews.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depts'] = department.objects.all()
        return context

class deptView(ListView):
    """

    Context variable in template -> "reviews"
    Template file -> "reviews/allReviews.html"
    """
    model = department
    context_object_name = "depts"
    template_name = "reviews/deptView.html"

class searchReviews(ListView):
    """
    Displays a list of reviews based on query
    
    Context variable in template -> "reviews" 
    Template file -> "reviews/searchReviews.html"
    """
    model = review
    context_object_name = "reviews"
    template_name = "reviews/searchReviews.html"
    paginate_by = 15
    
    def get_context_data(self, *args, **kwargs):
        # getting context variables so search terms can be referenced in searchReviews template
        context = super().get_context_data(*args, **kwargs)
        context['course_code'] = self.request.GET.get('course_code').upper()
        context['depts'] = department.objects.all()
        return context

    def get_queryset(self):
        #gets the desired course code from the form in searchReviews
        #adds space between dept and course num if there isn't one
        searchTerm = re.sub(r'(?<=[a-zA-Z])(?=\d)', ' ', self.request.GET.get('course_code').upper()).strip()
        print(searchTerm)
        if (any(char.isdigit() for char in searchTerm)):
        #locating the correct model attribute and generating query set
            courses = course.objects.filter(courseCode=searchTerm)
            queryset = review.objects.filter(course__in=courses)
            return queryset
        else:
            #search by dept
            # adding space so EN doesn't match ENG
            searchTerm += " "
            courses = course.objects.filter(courseCode__contains=searchTerm)
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depts'] = department.objects.all()
        return context


class createReview(LoginRequiredMixin, CreateView):
    """
    Displays a form for submitting a new review
    Context variable in template -> "review" 
    Template file -> "reviews/Review_form.html"
    """
    
    #We need to figure out what this method does exactly
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    context_object_name = "review"
    model = review
    fields = ('course', 'instructor', 'reviewText', 'anon')
    #review.user = request.user
    ##below is where we send the user after successfully submitting form
    success_url = reverse_lazy('reviews')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depts'] = department.objects.all()
        return context
    