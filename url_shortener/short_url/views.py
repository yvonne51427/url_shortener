from django.shortcuts import render, redirect
from .models import ShortURL
from django.http import HttpResponse

def create_short_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        short_url = ShortURL(original_url=original_url)
        short_url.save()
        return render(request, 'short_url/created.html', {'short_url': short_url})
    return render(request, 'short_url/create.html')

def redirect_to_url(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        short_url.click_count += 1
        short_url.save()
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return HttpResponse("Short URL does not exist", status=404)

def url_stats(request):
    urls = ShortURL.objects.all()
    return render(request, 'short_url/stats.html', {'urls': urls})

