from django.conf.urls import url
from . import views

app_name = 'user_notification'

urlpatterns = [
    url(r'^$', views.notification),
    url('^showDetails/', views.show_details, name="showDetails"),
]
