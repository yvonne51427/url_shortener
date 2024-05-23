from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import ShortUrl, URLClick

class ShortUrlTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

    def test_create_short_url(self):
        response = self.client.post('/api/short-urls/', {'original_url': 'http://example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ShortUrl.objects.count(), 1)

    def test_redirect_short_url(self):
        short_url = ShortUrl.objects.create(user=self.user, original_url='http://example.com')
        response = self.client.get(f'/api/r/{short_url.short_hash}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(URLClick.objects.count(), 1)

