from django import forms
from .models import Tournament, Match
from datetime import datetime


class TournamentForm(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text="Please enter the tournament name.")
    player1 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player2 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player3 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player4 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player5 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player6 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player7 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player8 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    date_created = forms.DateTimeField(initial=datetime.now())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tournament
        fields = ('name',)


class MatchForm(forms.ModelForm):
    player1 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    player2 = forms.CharField(max_length=250, help_text="Please enter the player's name.")
    score1 = forms.IntegerField(initial=0, help_text="Please enter the score.")
    score2 = forms.IntegerField(initial=0, help_text="Please enter the score.")

    CHOICES = (
        (1, 'Quarter'),
        (2, 'Semifinal'),
        (3, 'Final'),
    )
    round = forms.ChoiceField(choices=CHOICES, help_text="Please, select from the below")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Match
        fields = ('player1', 'player2', 'score1', 'score2', 'round')