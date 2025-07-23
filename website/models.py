from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=100, default="Sample Tour Title")
    description = models.TextField(default="Default tour description")
    # Add these two new fields:
    duration = models.CharField(max_length=50, default="X Days")
    difficulty = models.CharField(max_length=50, default="Easy")
    # ---
    image = models.ImageField(upload_to='tours/') # Requires Pillow
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE) 

    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    number_of_people = models.IntegerField(default=1)
    preferred_date = models.DateField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)

    booked_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Booking for {self.full_name} on {self.tour.title}"