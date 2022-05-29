from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

# Create your views here.
class GeekyShowsRedirectView(RedirectView):
    url = 'https://www.youtube.com/watch?v=udY9elNHhho&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=110'

class MeroJobRedirectView(RedirectView):
    pattern_name = 'redirectview_merojob'

class PkView(RedirectView):
    pattern_name = 'pk'
