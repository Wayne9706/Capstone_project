
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemListView.as_view(), name='menu-items'),
    path('menu-items/create/', views.MenuItemCreateView.as_view(), name='menu-item-create'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
]  