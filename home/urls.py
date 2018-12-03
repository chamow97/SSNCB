from django.conf.urls import url

from home import views

app_name='home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.enter, name='enter'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^construction', views.construction, name='construction'),
    url(r'^logout_user', views.logout_user, name='logout_user'),
    url(r'^editor', views.online_editor, name='online_editor'),
    url(r'^practice', views.practice, name='practice')

]