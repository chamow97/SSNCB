from django.conf.urls import url

from home import views

app_name='home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^register$', views.UserFormView.as_view(), name='register')
]