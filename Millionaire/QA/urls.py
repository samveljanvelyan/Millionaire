from QA import views
from django.conf.urls import url

app_name = 'QA'

urlpatterns = [
    url(r'^start/$', views.start_the_game, name='start')
]
