from django.urls import path
from .views import ShortUrlListCreateAPIView, ShortUrlStatsAPIView, RedirectShortUrlAPIView, ShortUrlCreateView, ShortUrlView

urlpatterns = [
    path('short-urls/', ShortUrlListCreateAPIView.as_view(), name='short_url_list_create'),
    path('short-urls/<int:pk>/stats/', ShortUrlStatsAPIView.as_view(), name='short_url_stats'),
    path('r/<str:short_hash>/', RedirectShortUrlAPIView.as_view(), name='redirect_short_url'),
    path('create/', ShortUrlCreateView.as_view(), name='create_short_url'),
    path('stats/', ShortUrlView.as_view(), name='url_stats'), 
]
