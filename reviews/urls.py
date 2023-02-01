from django.urls import path
from .views import allReviews
from .views import reviewDetails
from .models import review

urlpatterns = [

path("", allReviews.as_view(), name='reviews'),
path("review/<int:pk>/", reviewDetails.as_view(), name='review')
]