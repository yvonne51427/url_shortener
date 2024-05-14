from django.db import models
import uuid

class ShortURL(models.Model):
    # Define fields for the model where each field is represented as an instance of a field class
    original_url = models.URLField(max_length=2000)  # Field to store the original URL
    short_code = models.CharField(max_length=10, unique=True, blank=True)  # Field to store the short URL code
    click_count = models.IntegerField(default=0)  # Field to track the number of times the short URL is accessed
    created_at = models.DateTimeField(auto_now_add=True)  # Field to store the creation date and time of the short URL

    def save(self, *args, **kwargs):
        # Custom save method to generate a short code if it does not exist
        if not self.short_code:
            # Generate a unique short code using UUID, truncated to 6 characters
            self.short_code = uuid.uuid4().hex[:6]
        super().save(*args, **kwargs)  # Call the superclass method to handle default save functionality

    def __str__(self):
        # Human-readable representation of the model instance, showing the original and short URL
        return f'{self.original_url} to {self.short_code}'

