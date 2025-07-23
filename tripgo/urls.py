# tripgo/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin panel
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('website.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)