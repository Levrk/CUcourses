from django.urls import path
from .views import allReviews, reviewDetails, createReview, searchReviews
from .models import review, department, course

urlpatterns = [

path("all-reviews", allReviews.as_view(), name='reviews'),
path('search/', searchReviews.as_view(), name='search_reviews'),
path("review/<int:pk>/", reviewDetails.as_view(), name='review'),
path("create-review/", createReview.as_view(), name='create-review')
]