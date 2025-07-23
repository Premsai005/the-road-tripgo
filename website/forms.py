# website/forms.py

from django import forms
from .models import Booking,Review

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
    'min': 1,
    'max': 5,
    'placeholder': 'Enter a rating from 1 to 5',
    'class': 'form-control',
}),
            'comment': forms.Textarea(attrs={'placeholder': 'Share your experience...', 'rows': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating or rating < 1 or rating > 5:
            raise forms.ValidationError("Please select a star rating between 1 and 5.")
        return rating
