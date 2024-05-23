from rest_framework import serializers
from .models import ShortUrl, URLClick

class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['id', 'user', 'original_url', 'short_hash', 'created_at', 'click_count']

class URLClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLClick
        fields = ['id', 'short_url', 'ip_address', 'timestamp']
