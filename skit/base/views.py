from django.views import generic


# Index view
class IndexView(generic.TemplateView):
    template_name = 'base/home.html'
