from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import ShortUrl, URLClick
from .serializers import ShortUrlSerializer, URLClickSerializer
from django.http import JsonResponse

class ShortUrlListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all short URLs and create a new short URL.
    """
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new short URL with the current user.
        """
        serializer.save(user=self.request.user)

class ShortUrlStatsAPIView(APIView):
    """
    API view to retrieve click statistics for a specific short URL.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        short_url = get_object_or_404(ShortUrl, pk=pk)
        clicks = URLClick.objects.filter(short_url=short_url)
        serializer = URLClickSerializer(clicks, many=True)
        return Response(serializer.data)

class RedirectShortUrlAPIView(APIView):
    """
    API view to handle redirection from a short URL to the original URL.

    Note: This view does not require authentication because it is intended to be publicly accessible 
    to anyone using the short URL.
    """
    def get(self, request, short_hash):
        short_url = get_object_or_404(ShortUrl, short_hash=short_hash)
        URLClick.objects.create(short_url=short_url, ip_address=request.META.get('REMOTE_ADDR', ''))
        short_url.click_count += 1
        short_url.save()
        return redirect(short_url.original_url)

class ShortUrlCreateView(APIView):
    """
    API view to handle the creation of short URLs through a web interface.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Render the form to create a new short URL.
        """
        short_urls = ShortUrl.objects.filter(user=request.user)
        return render(request, 'short_url/create_short_url.html', {'short_urls': short_urls})

    def post(self, request):
        """
        Create a new short URL.
        """
        original_url = request.POST.get('original_url')
        existing_short_url = ShortUrl.objects.filter(original_url=original_url, user=request.user).first()
        if existing_short_url:
            return JsonResponse({'message': 'Short URL already exists', 'short_hash': existing_short_url.short_hash})
        short_url = ShortUrl(user=request.user, original_url=original_url)
        short_url.save()
        return JsonResponse({'message': 'Short URL created successfully', 'short_hash': short_url.short_hash})

class ShortUrlView(APIView):
    """
    API view to display the user's short URLs and their statistics.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        short_urls = ShortUrl.objects.filter(user=request.user)
        return render(request, 'short_url/url_stats.html', {'short_urls': short_urls})
