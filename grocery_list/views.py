from django.views import generic
from .models import Grocery
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# use the mixin in the edit and/on delete classes


class GroceryList(LoginRequiredMixin, generic.ListView):
    """
    Render grocery shopping list
    """
    model = Grocery
    queryset = Grocery.objects.order_by('-created_on')
    template_name = 'grocery_list/create_list.html'
    context_object_name = 'grocerys'

    def get_queryset(self, **kwargs):
        grocerys = self.model.objects.filter(user=self.request.user)
        return grocerys
