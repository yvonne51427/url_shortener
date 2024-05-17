from django.contrib import admin
from .models import ShortUrl, URLClick

admin.site.register(ShortUrl)
admin.site.register(URLClick)
