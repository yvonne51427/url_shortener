from rest_framework import serializers
from .models import ShortUrl, URLClick

class ShortUrlSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShortUrl model.
    
    This serializer converts the ShortUrl model instance to and from JSON format.
    
    Fields:
        id: The primary key of the ShortUrl instance.
        user: The user who created the short URL.
        original_url: The original URL to be shortened.
        short_hash: The unique short hash representing the short URL.
        created_at: The timestamp when the short URL was created.
        click_count: The count of clicks the short URL has been clicked.
    """
    class Meta:
        model = ShortUrl
        fields = ['id', 'user', 'original_url', 'short_hash', 'created_at', 'click_count']

class URLClickSerializer(serializers.ModelSerializer):
    """
    Serializer for the URLClick model.
    
    This serializer converts the URLClick model instance to and from JSON format.
    
    Fields:
        id: The primary key of the URLClick instance.
        short_url: The short URL that was clicked.
        ip_address: The IP address from which the click was made.
        timestamp: The timestamp when the click occurred.
    """
    class Meta:
        model = URLClick
        fields = ['id', 'short_url', 'ip_address', 'timestamp']
