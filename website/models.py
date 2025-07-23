from django.db import models
from django.conf import settings


class Tour(models.Model):
    title = models.CharField(max_length=100, default="Sample Tour Title")
    description = models.TextField(default="Default tour description")
    duration = models.CharField(max_length=50, default="X Days")
    difficulty = models.CharField(max_length=50, default="Easy")
    image = models.ImageField(upload_to='tours/')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"
        ordering = ['title']


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    number_of_people = models.IntegerField(default=1)
    preferred_date = models.DateField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.full_name} on {self.tour.title} ({self.preferred_date or 'No Date Specified'})"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-booked_at']


class Review(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Review for {self.tour.title} - Rating: {self.rating}"
    
class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='stories/') # Image for the person/experience
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"
        ordering = ['-created_at'] # Show most recent stories first

    def __str__(self):
        return self.title