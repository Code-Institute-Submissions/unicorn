from django.conf.urls import url
from .views import tickets

urlpatterns = [
    url(r'^$', tickets, name='tickets'),
]