# website/forms.py

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    
    preferred_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=False
    )

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number', 'number_of_people', 'preferred_date', 'special_requests']
        
        labels = {
            'full_name': 'Your Full Name',
            'phone_number': 'Phone Number (Optional)',
            'number_of_people': 'Number of Travelers',
            'preferred_date': 'Preferred Travel Date (Optional)',
            'special_requests': 'Special Requests (Optional)',
        }
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 4}), 
        }