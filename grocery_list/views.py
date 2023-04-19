from django.views import generic


class LandingPage(generic.TemplateView):
    template_name = 'grocery_list/home.html'
