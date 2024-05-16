from django.db import models
from django.contrib.auth.models import User
import hashlib
import random
import string

class ShortUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_hash = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_hash:
            self.short_hash = self.generate_unique_short_hash()
        super().save(*args, **kwargs)

    def generate_unique_short_hash(self):
        while True:
            hash_part = hashlib.md5(self.original_url.encode()).hexdigest()[:5]
            random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            short_hash = hash_part + random_part
            if not ShortUrl.objects.filter(short_hash=short_hash).exists():
                return short_hash

    def __str__(self):
        return f'{self.original_url} -> {self.short_hash}'

class URLClick(models.Model):
    short_url = models.ForeignKey(ShortUrl, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.short_url} clicked from {self.ip_address} at {self.timestamp}'
