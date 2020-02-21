from django.conf.urls import url
from login_registration import views

app_name = 'login_registration'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login')
]
