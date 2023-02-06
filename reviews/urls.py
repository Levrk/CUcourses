from django.urls import path
from .views import allReviews, reviewDetails, createReview
from .models import review, department, course

urlpatterns = [

path("all-reviews", allReviews.as_view(), name='reviews'),
path("review/<int:pk>/", reviewDetails.as_view(), name='review'),
path("create-review/", createReview.as_view(), name='create-review')
]