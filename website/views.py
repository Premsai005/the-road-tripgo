# website/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Booking, Review ,Story # Added Review
from .forms import BookingForm, ReviewForm  # Added ReviewForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse

def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'index.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('login')
    return redirect('home')

def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            # Removed the line linking booking.user as there is no user element
            booking.save()

            messages.success(request, "Your booking request has been received!")
            return redirect('booking_success')

        else:
            messages.error(request, "Please correct the errors in the booking form.")
    else:
        # Removed initial_data related to request.user as there is no user element
        form = BookingForm()

    context = {
        'tour': tour,
        'form': form,
    }
    return render(request, 'tour_detail.html', context)

def booking_success_view(request):
    return render(request, 'booking_success.html')

def submit_review_view(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.save()
            messages.success(request, "Thank you for your review!")
            return redirect('tour_detail', tour_id=tour.id) # Redirect back to the tour detail page
        else:
            messages.error(request, "There was an error submitting your review. Please correct the errors.")
    else:
        form = ReviewForm()

    context = {
        'tour': tour,
        'form': form,
    }
    return render(request, 'review.html', context)

def index(request):
    tours = Tour.objects.all()
    stories = Story.objects.all().order_by('-created_at') # Fetch all stories
    context = {
        'tours': tours,
        'stories': stories, # Add stories to the context
    }
    return render(request, 'index.html', context)