# website/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Booking 
from .forms import BookingForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse

# View for your main index page, displaying tours
def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'index.html', context)

# View for user registration (Sign Up)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! Welcome!")
            # Fix the NoReverseMatch here: use 'home' instead of 'index'
            return redirect('home') # Corrected URL name to 'home'
        else:
            # If form is not valid, pass the form with errors back to the template
            # You can also iterate form.errors.items() to add specific messages per field
            messages.error(request, "Signup failed. Please correct the errors below.")
            # The form with errors will automatically be passed to the template
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# View for user login
def login_view(request):
    if request.method == 'POST':
        # AuthenticationForm takes 'request' as the first argument, then 'data'
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            # Handle 'next' parameter for redirecting to the intended page
            next_url = request.POST.get('next') or request.GET.get('next') # Check both POST and GET for 'next'
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home') # Corrected URL name to 'home'
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View for user logout
def logout_view(request):
    # Ensure logout only happens for POST request for security
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('login') # Redirect to the login page after logout
    # For GET requests to /logout/, redirect to home or login as it's not a valid logout action
    return redirect('home') # Or redirect('login') if you prefer for GET /logout/

def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id) # Get the Tour object or return 404

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False) # Create booking object but don't save yet
            booking.tour = tour # Link the booking to the current tour
            if request.user.is_authenticated:
                booking.user = request.user # Link to logged-in user if applicable
            booking.save() # Save the booking to your Django database

            messages.success(request, "Your booking request has been received!")

            # --- Google Form Integration (Client-side redirect) ---
            # IMPORTANT: Replace with YOUR Google Form's publish URL and entry IDs
            # You'll need to set up a Google Form and get these values.
            # Instructions below on how to find these.
            google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfmYxiGqtjhfovkVsK3_fcDA9w0p_tadXezohqu5a-5-eBhdQ/viewform?usp=pp_url&entry.2005620554=prem&entry.1045781291=p2514958@gmail.com&entry.1166974658=9391166435&entry.839337160=2&entry.738658398=2025-07-25"
            entry_ids = {
                "full_name": "2005620554",
                "email": "1045781291",
                "phone_number": "1166974658",
                "number_of_people": "839337160",
                "preferred_date": "738658398",
                "special_requests": "663558033",
                
            }

            google_form_redirect_url = f"{google_form_url}?"
            google_form_redirect_url += f"entry.{entry_ids['full_name']}={form.cleaned_data['full_name']}&"
            google_form_redirect_url += f"entry.{entry_ids['email']}={form.cleaned_data['email']}&"
            google_form_redirect_url += f"entry.{entry_ids['phone_number']}={form.cleaned_data['phone_number'] or ''}&"
            google_form_redirect_url += f"entry.{entry_ids['number_of_people']}={form.cleaned_data['number_of_people']}&"
            google_form_redirect_url += f"entry.{entry_ids['preferred_date']}={form.cleaned_data['preferred_date'] or ''}&"
            google_form_redirect_url += f"entry.{entry_ids['special_requests']}={form.cleaned_data['special_requests'] or ''}"

            return redirect(google_form_redirect_url)

        else:
            messages.error(request, "Please correct the errors in the booking form.")
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'full_name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = BookingForm(initial=initial_data)

    context = {
        'tour': tour,
        'form': form,
    }
    return render(request, 'tour_detail.html', context)