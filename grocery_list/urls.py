from .views import LandingPage, GroceryList
from django.urls import path


urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    path('create_list', GroceryList.as_view(), name='grocery_list')
]
