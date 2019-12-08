from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),     #r-> regex, url-> raw url, ^-> start, $-> end
    # url(r'^$', views.homepage),
    url(r"^create/$", views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_details, name='detail')
]
