from django.urls import path
from .views import reviewDetails, createReview, searchReviews, CustomLoginView, RegisterPage, HomeView
from .models import review, department, course
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest



urlpatterns = [

path("login/", CustomLoginView.as_view(), name ='login'),    
path("logout/", LogoutView.as_view(next_page ='homePage'), name ='logout'), 
path('register/', RegisterPage.as_view(), name= 'register'),
path('search/', searchReviews.as_view(), name='search_reviews'),
path("review/<int:pk>/", reviewDetails.as_view(), name='review'),
path("create-review/", createReview.as_view(), name='create-review'),
path("", HomeView.as_view(), name='homePage')
]