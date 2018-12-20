from django.test import TestCase

from apps.ping.models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(code="bastionhost", link="http://bastionhost.org")

    def test_animals_can_speak(self):
        company = Company.objects.filter(code="bastionhost").first()
        self.assertEqual(company.link, "http://bastionhost.org")
