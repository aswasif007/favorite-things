from django.test import TestCase, Client

from rest_framework import status

from .models import Category, Item, Rank


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


class TestSingleCategoryView(TestCase):

    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(title='test_cat_1')
        self.endpoint = f'/api/v0/categories/{self.category.guid}'

    def test_get(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_category = response.json()
        expected_category = self.category

        assertObjects(expected_category, returned_category, ['guid', 'title', 'color_code'])

    def test_put(self):
        response = self.client.put(self.endpoint, data={'title': 'new_title'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_category = response.json()
        self.category.refresh_from_db()
        expected_category = self.category

        assertObjects(expected_category, returned_category, ['title'])

    def test_patch(self):
        response = self.client.patch(self.endpoint, data={'color_code': '#122'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_category = response.json()
        self.category.refresh_from_db()
        expected_category = self.category

        assertObjects(expected_category, returned_category, ['color_code'])

    def test_delete(self):
        response = self.client.delete(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Category.DoesNotExist):
            self.category.refresh_from_db()


class TestItemView(TestCase):

    def setUp(self):
        self.client = Client()
        self.endpoint = '/api/v0/items/'
        self.category = Category.objects.create(title='test_category')

    def test_get(self):
        Item.objects.create(title='test_item_1', category=self.category, metadata={'foo': 'bar'})
        Item.objects.create(title='test_item_2', category=self.category, description='foo bar')

        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_items = response.json()
        expected_items = Item.objects.all()
        self.assertEqual(len(expected_items), len(returned_items))

        for expected_item, returned_item in zip(expected_items, returned_items):
            assertObjects(expected_item, returned_item, ['guid', 'title', 'description', 'metadata', 'rank'])
            self.assertEqual(expected_item.category.guid, returned_item['category'])

    def test_create(self):
        request_body = {
            'title': 'test_item_3',
            'category': self.category.guid,
            'description': 'foo bar',
            'metadata': {'foo': 'bar'}
        }
        response = self.client.post(self.endpoint, data=request_body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        returned_item = response.json()
        expected_item = Item.objects.get(guid=returned_item['guid'])

        assertObjects(expected_item, returned_item, ['title', 'description', 'metadata', 'rank'])
        self.assertEqual(expected_item.category.guid, returned_item['category'])
        self.assertEqual(expected_item.rank, Item.objects.count())


class TestSingleItemApiView(TestCase):

    def setUp(self):
        self.client = Client()

        self.category = Category.objects.create(title='category')
        self.item = Item.objects.create(
            title='item',
            category=self.category,
            description='foo',
            metadata={'foo': 'bar'},
        )
        self.endpoint = f'/api/v0/items/{self.item.guid}'

    def test_get(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_item = response.json()
        expected_item = self.item

        assertObjects(expected_item, returned_item, ['guid', 'title', 'description', 'metadata', 'rank'])

    def test_put(self):
        request_body = {'title': 'new_title', 'category': self.category.guid}
        response = self.client.put(self.endpoint, data=request_body, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_item = response.json()
        self.item.refresh_from_db()
        expected_item = self.item

        assertObjects(expected_item, returned_item, ['title'])

    def test_patch(self):
        response = self.client.patch(self.endpoint, data={'description': 'foo'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_item = response.json()
        self.item.refresh_from_db()
        expected_item = self.item

        assertObjects(expected_item, returned_item, ['description'])

    def test_delete(self):
        response = self.client.delete(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        rank = Rank.objects.first()
        self.assertNotIn(self.item.guid, rank.data)

        sorted_rank_data = sorted(rank.data.values())
        self.assertListEqual(sorted_rank_data, list(range(1, Item.objects.count() + 1)))

        with self.assertRaises(Item.DoesNotExist):
            self.item.refresh_from_db()


class TestSingleItemRankView(TestCase):

    def setUp(self):
        self.client = Client()

        category = Category.objects.create(title='category')
        self.item_1 = Item.objects.create(title='item_1', category=category)
        self.item_2 = Item.objects.create(title='item_2', category=category)
        self.endpoint = f'/api/v0/items/{self.item_2.guid}/rank'

    def test_get(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        returned_data = response.json()
        expected_data = self.item_2

        assertObjects(expected_data, returned_data, ['guid', 'rank'])

    def test_update(self):
        response = self.client.put(self.endpoint, data={'rank': 1}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.item_1.refresh_from_db()
        self.assertEqual(self.item_1.rank, 2)
        
        self.item_2.refresh_from_db()
        self.assertEqual(self.item_2.rank, 1)
