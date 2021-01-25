from django.conf.urls import url

from web.views import index

urlpatterns = [
    url('index/', index, name='index')
]
