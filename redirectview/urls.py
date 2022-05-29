from re import template
from django.urls import path
from redirectview import views
urlpatterns = [
    path('',views.TemplateView.as_view(template_name='school/home.html'),name='redirectview'),
    path('home/',views.RedirectView.as_view(url='/redirectview'),name='redirectview_home'),
    # path('index/',views.RedirectView.as_view(url='/redirectview'),name='redirectview_index'),
    path('youtube/',views.RedirectView.as_view(url='https://www.youtube.com/watch?v=udY9elNHhho&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=110'),name='redirectview_youtube'),
    path('geekyshows/',views.GeekyShowsRedirectView.as_view(),name='redirectview_geekyshows'),
    path('index/',views.RedirectView.as_view(pattern_name='redirectview_home')),
    path('merojob/',views.RedirectView.as_view(url='https://merojob.com/'),name='redirectview_merojob'),
    path('hamrojob/',views.MeroJobRedirectView.as_view()),
    path('home/<int:pk>/',views.PkView.as_view(),name='pkhome'),
    path('<int:pk>/',views.TemplateView.as_view(template_name='school/home.html'),name='pk'),
]
