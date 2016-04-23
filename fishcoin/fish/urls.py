


from django.conf.urls import url
from fish import views

urlpatterns = [
    url(r'^fish/$', views.fish_list),
    url(r'^fish/(?P<pk>[0-9]+)/$', views.fish_detail),
]
