from django.conf.urls import url, include

from apps.goods import views

urlpatterns = [

    url('^index', views.IndexView.as_view(), name='index'),

]
