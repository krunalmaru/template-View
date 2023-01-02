from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Myview(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Raj'
        context['roll'] = 101
        # context ={'name':'raj','roll':101}
        return context

