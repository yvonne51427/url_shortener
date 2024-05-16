from django.shortcuts import render, redirect
from django.urls import reverse

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def data_deletion(request):
    return render(request, 'data_deletion.html')

def custom_login(request):
    return render(request, 'account/custom_login.html')

def redirect_to_login(request):
    return redirect(reverse('account_login'))
