from django.views import generic
# from .models import Grocery


class LandingPage(generic.TemplateView):
    template_name = 'grocery_list/home.html'


# class CreateList(generic.ListView):
#     model = Grocery
#     template_name = 'grocery_list/create_list.html'
