# website/admin.py

from django.contrib import admin
from .models import Tour,Booking,Review,Story
  # Import your model

admin.site.register(Tour)  # Register it with the admin site
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Story)
