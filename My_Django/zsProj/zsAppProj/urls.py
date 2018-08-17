from django.conf.urls import url
from zsAppProj import views

urlpatterns = [
    url(r'^$', views.zsAppProj, name='zsAppProj')

]
