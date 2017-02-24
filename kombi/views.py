""" Application views """

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from kombi.forms import RegisterForm

class IndexView(TemplateView):
    """ Main index view """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        """ Function to generate template context """
        context = super(IndexView, self).get_context_data(**kwargs)
        context['appname'] = settings.APP_NAME
        return context

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/thanks/'
    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)
