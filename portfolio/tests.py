from django.test import TestCase
from django.urls import reverse

from .models import Category, PortfolioItem, Tag


class PortfolioSearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        coding = Category.objects.create(name=Category.CODING)
        ads = Category.objects.create(name=Category.ADVERTISING)

        py_tag = Tag.objects.create(name='python')
        ads_tag = Tag.objects.create(name='digital-ads')

        cls.item_coding = PortfolioItem.objects.create(
            title='My Django App',
            description='A web application built with Django and Python.',
            category=coding,
            url='https://example.com',
        )
        cls.item_coding.tags.add(py_tag)

        cls.item_ads = PortfolioItem.objects.create(
            title='Social Media Campaign',
            description='A successful advertising campaign on social platforms.',
            category=ads,
        )
        cls.item_ads.tags.add(ads_tag)

    def test_home_page_loads(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')
        self.assertContains(response, 'Social Media Campaign')

    def test_search_by_title(self):
        response = self.client.get(reverse('portfolio:home'), {'q': 'Django'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')
        self.assertNotContains(response, 'Social Media Campaign')

    def test_search_by_description(self):
        response = self.client.get(reverse('portfolio:home'), {'q': 'advertising'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Social Media Campaign')
        self.assertNotContains(response, 'My Django App')

    def test_search_by_tag(self):
        response = self.client.get(reverse('portfolio:home'), {'q': 'python'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')

    def test_search_no_results(self):
        response = self.client.get(reverse('portfolio:home'), {'q': 'xyznotfound'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No results found')

    def test_filter_by_category(self):
        response = self.client.get(
            reverse('portfolio:home'), {'category': Category.CODING}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')
        self.assertNotContains(response, 'Social Media Campaign')

    def test_filter_by_tag(self):
        response = self.client.get(reverse('portfolio:home'), {'tag': 'python'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')
        self.assertNotContains(response, 'Social Media Campaign')

    def test_detail_page_loads(self):
        response = self.client.get(
            reverse('portfolio:item_detail', kwargs={'pk': self.item_coding.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Django App')
        self.assertContains(response, 'A web application built with Django and Python.')

    def test_detail_page_404(self):
        response = self.client.get(
            reverse('portfolio:item_detail', kwargs={'pk': 9999})
        )
        self.assertEqual(response.status_code, 404)

    def test_result_count_shown(self):
        response = self.client.get(reverse('portfolio:home'), {'q': 'Django'})
        self.assertContains(response, '1 project found')
