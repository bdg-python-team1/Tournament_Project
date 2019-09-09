from django.contrib import admin
from .models import Tournament, Match


class TournamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match)