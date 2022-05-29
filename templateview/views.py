from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class CustomView(TemplateView):
    template_name = 'templateview_custom.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['custom'] = 'This is custom test for templateview'
        # context = {'custom':'This is custom test for templateview'} ==> extra_context will not work if we define context this way
        return context