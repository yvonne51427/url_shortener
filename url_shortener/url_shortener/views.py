from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from short_url.models import ShortUrl
#from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
#from allauth.socialaccount.providers.oauth2.client import OAuth2Client
#from allauth.socialaccount.helpers import complete_social_login
#from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
#from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def data_deletion(request):
    return render(request, 'data_deletion.html')

def custom_login(request):
    return render(request, 'account/custom_login.html')

def redirect_to_login(request):
    return redirect('account_login')

@login_required
def create_short_url_view(request):
    short_urls = ShortUrl.objects.filter(user=request.user)
    return render(request, 'short_url/create_short_url.html', {'short_urls': short_urls})

#def login_with_google(request):
#    google_login_url = reverse('account_login')
#    return redirect(google_login_url)
#
#def login_with_facebook(request):
#    facebook_login_url = reverse('account_login')
#    return redirect(facebook_login_url)
