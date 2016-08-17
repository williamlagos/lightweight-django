""" Application views """

from django.views.generic.base import TemplateView
from django.conf import settings

class IndexView(TemplateView):
    """ Main index view """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        """ Function to generate template context """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['appname'] = settings.APP_NAME
        return context
