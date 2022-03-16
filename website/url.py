from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', (admin.site.urls)),
    url(r'^$', views.button_search),
    url(r'^get_mesh', views.get_mesh, name='script')
]
