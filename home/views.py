from django.views import generic


class LandingPage(generic.TemplateView):
    """
    Render the landing page to the UI
    """
    template_name = 'home/landing.html'
