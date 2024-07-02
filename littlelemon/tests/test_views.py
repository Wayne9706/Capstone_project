from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Cake", price=120, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Pie", price=60, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)