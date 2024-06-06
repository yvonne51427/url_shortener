from django.db import models
from django.contrib.auth.models import User
import hashlib
import random
import string

class ShortUrl(models.Model):
    """
    Model representing a short URL.

    Attributes:
        user (ForeignKey): The user who created the short URL.
        original_url (URLField): The original URL to be shortened.
        short_hash (CharField): The unique short hash representing the short URL.
        created_at (DateTimeField): The timestamp when the short URL was created.
        click_count (IntegerField): The count of clicks the short URL has been clicked.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_hash = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        Save method override to generate a unique short hash if not already set.
        """
        if not self.short_hash:
            self.short_hash = self.generate_unique_short_hash()
        super().save(*args, **kwargs)

    def generate_unique_short_hash(self):
        """
        Generate a unique short hash for the URL.

        Returns:
            str: A unique short hash combining MD5 and random characters.
        """
        while True:
            hash_part = hashlib.md5(self.original_url.encode()).hexdigest()[:5]
            random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            short_hash = hash_part + random_part
            # Ensure the generated hash is unique
            if not ShortUrl.objects.filter(short_hash=short_hash).exists():
                return short_hash

    def __str__(self):
        """
        String representation of the ShortUrl instance.
        """
        return f'{self.original_url} -> {self.short_hash}'

class URLClick(models.Model):
    """
    Model representing a click on a short URL.

    Attributes:
        short_url (ForeignKey): The short URL that was clicked.
        ip_address (GenericIPAddressField): The IP address from which the click was made.
        timestamp (DateTimeField): The timestamp when the click occurred.
    """
    short_url = models.ForeignKey(ShortUrl, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the URLClick instance.
        """
        return f'{self.short_url} clicked from {self.ip_address} at {self.timestamp}'
