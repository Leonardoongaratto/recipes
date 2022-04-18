from django.test import TestCase
from django.urls import reverse, resolve


class RecipeURLsTest(TestCase):
    def test_recipe_url_home_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')


    def test_recipe_category_url_home_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 2})
        self.assertEqual(url, '/recipes/category/2/')


    def test_recipe_detail_url_home_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 2})
        self.assertEqual(url, '/recipes/2/')


    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')       