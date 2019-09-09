from django.shortcuts import render
from .models import Tournament, Match

def home(request):
    tournament_list = Tournament.objects.all()
    context_dict = {}
    context_dict['message'] = "All Tournaments"
    context_dict['tournaments'] = tournament_list
    return render(request, 'contest/home.html', context_dict)
