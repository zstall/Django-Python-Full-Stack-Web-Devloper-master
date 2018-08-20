from django.conf.urls import url
from user_app import views

urlpatterns = [
    url(r'^$', views.user_app, name='user'),

]
