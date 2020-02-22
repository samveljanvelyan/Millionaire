from QA import views
from django.conf.urls import url

app_name = 'QA'

urlpatterns = [
    url(r'^start/$', views.start_the_game, name='start'),
    url(r'result/$', views.game_result, name='result'),
    url(r'leader_board/$', views.show_leader_board, name='leader_board')
]
