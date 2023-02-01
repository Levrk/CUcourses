from django.contrib import admin

# Register your models here.
from .models import review
from .models import course
from .models import department
# Register your models here.

admin.site.register(review)
admin.site.register(course)
admin.site.register(department)