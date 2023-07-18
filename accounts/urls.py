from django.conf.urls import url
from . import views
appName = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.signupUser, name="signup"),
    url(r'^login/$', views.loginUser, name="login"),
    url(r'^logout/$', views.logoutUser, name="logout"),
]