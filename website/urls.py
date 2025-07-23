# website/urls.py

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('tour/<int:tour_id>/', views.tour_detail_view, name='tour_detail'),
    path('booking/success/', views.booking_success_view, name='booking_success'),
    path('tours/<int:tour_id>/review/', views.submit_review_view, name='submit_review'),
    ]