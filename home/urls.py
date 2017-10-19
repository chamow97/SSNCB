from django.conf.urls import url

from home import views

app_name='home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enter$', views.enter, name='enter'),
    url(r'^register$', views.UserFormView.as_view(), name='register'),
    url(r'^construction', views.construction, name='construction'),
    url(r'^logout_user', views.logout_user, name='logout_user'),

]