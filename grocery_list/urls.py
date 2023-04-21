from .views import LandingPage
# from . import views
from django.urls import path


urlpatterns = [
    path('', LandingPage.as_view(), name='home'),
    # path('', views.CreateList.as_view(), name='create_list')
]
