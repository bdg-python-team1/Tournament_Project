from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tournament/<slug:tournament_name_slug>/', views.tournament_detail, name='tournament-detail'),
    path('add_tournament', views.add_tournament, name='add_tournament')
]