from django.test import TestCase, Client

from rest_framework import status

from .models import Category


def assertObjects(db_object, json_dict, fields):
    for field in fields:
        assert getattr(db_object, field) == json_dict[field], f'{getattr(db_object, field)} != {json_dict[field]}'


class TestCategoryView(TestCase):

    def setUp(self):
        self.client = Client()
        self.endpoint = '/api/v0/categories/'

    def test_get(self):
        Category.objects.create(title='test_cat_1')
        Category.objects.create(title='test_cat_2')

        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_categories = response.json()
        expected_categories = Category.objects.all()
        self.assertEqual(len(expected_categories), len(returned_categories))

        for expected_category, returned_category in zip(expected_categories, returned_categories):
            assertObjects(expected_category, returned_category, ['guid', 'title', 'color_code'])

    def test_create(self):
        response = self.client.post(self.endpoint, data={'title': 'test_cat_3', 'color_code': '#123'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        returned_category = response.json()
        expected_category = Category.objects.get(guid=returned_category['guid'])

        assertObjects(expected_category, returned_category, ['title', 'color_code'])
