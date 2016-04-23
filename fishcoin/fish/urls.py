


from django.conf.urls import url
from fish import views

urlpatterns = [
    url(r'^snippets/$', views.fish_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.fish_detail),
]
