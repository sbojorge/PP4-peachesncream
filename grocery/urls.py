from .views import GroceryList
from django.urls import path


urlpatterns = [
    path('create_list', GroceryList.as_view(), name='grocery_list')
]
