from django.urls import path
# from .views import LandingPage
from .views import CreateList

urlpatterns = [
    # path('', LandingPage.as_view(), name='home'),
    path('', CreateList.as_view(), name='create_list')
]
