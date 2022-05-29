from django.urls import path
from django.views.generic.base import TemplateView
from templateview import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='templateview.html',extra_context={'name':'Peter'}),name='templateview'),
    path('about/',TemplateView.as_view(template_name='templateview_about.html',extra_context={'add':'Queens'}),name='templateview_about'),
    # path('custom/',views.CustomView.as_view(extra_context={'extra':'This is extra context'}),name='templateview_custom'),
    path('custom/',views.CustomView.as_view(),name='templateview_custom'),
]