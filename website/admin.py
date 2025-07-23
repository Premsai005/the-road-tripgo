# website/admin.py

from django.contrib import admin
from .models import Tour  # Import your model

admin.site.register(Tour)  # Register it with the admin site
