from django.test import TestCase
from .models import Ad, ExchangeProposal
from django.contrib.auth.models import User

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.ad = Ad.objects.create(user=self.user, title='Test Ad', description='Test Description', category='Test', condition='new')

    def test_ad_creation(self):
        self.assertEqual(self.ad.title, 'Test Ad')

    def test_ad_deletion(self):
        self.ad.delete()
        self.assertFalse(Ad.objects.filter(id=self.ad.id).exists())
