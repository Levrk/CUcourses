from django.urls import path
from .views import reviewList
from .models import review

urlpatterns = [

path("", reviewList.as_view(), name='reviews')

]