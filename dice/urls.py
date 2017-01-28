from django.conf.urls import url

from . import views

app_name = 'dice'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]
