from django.views import generic
from .models import Grocery 


class LandingPage(generic.TemplateView):
    """
    Render the landing page to the UI
    """
    template_name = 'grocery_list/home.html'

class AddItem(generic.CreateView):
    """
    Add grocery item to the shopping list
    """
    

