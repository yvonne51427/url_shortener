from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_short_url, name='create_short_url'),
    path('stats/', views.url_stats, name='url_stats'),
    path('confirm/', views.confirm_existing_url, name='confirm_existing_url'),
    path('r/<str:short_hash>/', views.redirect_short_url, name='redirect_short_url'),
]
