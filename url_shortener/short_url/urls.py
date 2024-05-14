from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_short_url, name='create_short_url'),
    path('s/<str:short_url>/', views.redirect_to_url, name='redirect_to_url'),
    path('stats/', views.url_stats, name='url_stats'),
]
