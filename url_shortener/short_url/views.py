from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortUrl, URLClick
from .forms import ShortUrlForm
from django.contrib.auth.decorators import login_required

@login_required
def create_short_url(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            existing_short_url = ShortUrl.objects.filter(original_url=original_url, user=request.user).first()
            if existing_short_url:
                context = {
                    'form': form,
                    'existing_short_url': existing_short_url,
                }
                return render(request, 'short_url/confirm_existing_url.html', context)
            else:
                short_url = form.save(commit=False)
                short_url.user = request.user
                short_url.save()
                return redirect('url_stats')
    else:
        form = ShortUrlForm()
    return render(request, 'short_url/create_short_url.html', {'form': form})

@login_required
def confirm_existing_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        action = request.POST.get('action')
        if action == 'use_existing':
            short_url = ShortUrl.objects.get(original_url=original_url, user=request.user)
            return redirect('url_stats')
        elif action == 'create_new':
            short_url = ShortUrl(original_url=original_url, user=request.user)
            short_url.short_hash = short_url.generate_unique_short_hash()
            short_url.save()
            return redirect('url_stats')
    return redirect('create_short_url')

@login_required
def url_stats(request):
    short_urls = ShortUrl.objects.filter(user=request.user)
    context = {
        'short_urls': short_urls,
    }
    return render(request, 'short_url/url_stats.html', context)

def redirect_short_url(request, short_hash):
    short_url = get_object_or_404(ShortUrl, short_hash=short_hash)
    URLClick.objects.create(short_url=short_url, ip_address=request.META['REMOTE_ADDR'])
    short_url.click_count += 1
    short_url.save()
    return redirect(short_url.original_url)
