from django.urls import path
from . import views
from users import views as users_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('tournament/<slug:tournament_name_slug>/', views.tournament_detail, name='tournament-detail'),
    path('add_tournament/', views.AddTournamentView.as_view(), name='add_tournament'),
    path('profile/<username>/', users_view.ProfileView.as_view(), name='profile'),
    path('profiles/', users_view.ListProfilesView.as_view(), name='list_profiles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
