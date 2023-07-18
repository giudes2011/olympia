from django.conf.urls import url
from . import views
appName = 'articles'
urlpatterns = [
    url(r'^$', views.artiList, name="list"),
    url(r'^create/$', views.articleCreateForm, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.artiDetail, name="detail"),
]
