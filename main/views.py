from django.http import request
from django.shortcuts import render, get_object_or_404
from django import views
from .models import *
from datetime import date

from main.models import Club


class HomeView(views.View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(views.View):
    def get(self, request):

        clubs = Club.objects.all()
        context = {'clubs': clubs}

        return render(request, 'clubs.html', context)

class ClubDetailView(views.View):
    def get(self, request, pk):

        club = get_object_or_404(Club, id=pk)
        players = club.player_set.order_by('-price')

        context = {
            'club': club,
            'players': players
             }

        return render(request, 'clubdetails.html', context)

class LatestClubsView(views.View):

    def get(self, request):

        transfers = Transfer.objects.filter(season_id=Season.objects.last())

        context = {'transfers': transfers}

        return render(request, 'latest-transfers.html', context)

class PlayersView(views.View):

    def get(self, request):
        players = Player.objects.order_by('-price')

        context = {'players': players}

        return render(request, 'players.html', context)


class Player_U20View(views.View):

    def get(self, request):

        today = date.today()
        limit_year = today.year - 20

        players = Player.objects.filter(birth_date__year__gt=limit_year)

        context = {'players': players}
        return render(request, 'player_u20.html', context)



class TryoutsView(views.View):
    def get(self, request):
        return render(request, 'tryouts.html')