from django.urls import path
from django.views.generic.base import TemplateView
from .views import index

urlpatterns = [
    path('data',index,name="listener"),
]