from django.shortcuts import render
from .models import Tournament, Match

def home(request):
    tournament_list = Tournament.objects.all()
    context_dict = {}
    context_dict['message'] = "All Tournaments"
    context_dict['tournaments'] = tournament_list
    return render(request, 'contest/home.html', context_dict)

def tournament_detail(request, tournament_name_slug):
    context_dict = {}
    try:
        tournament = Tournament.objects.get(slug=tournament_name_slug)
        matches = Match.objects.filter(tournament=tournament)
        context_dict['matches'] = matches
        context_dict['tournament'] = tournament
    except Tournament.DoesNotExist:
        context_dict['tournament'] = None
        context_dict['matches'] = None

    return render(request, 'contest/tournament_detail.html', context_dict)