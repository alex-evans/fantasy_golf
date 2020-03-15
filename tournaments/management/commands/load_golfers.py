from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from tournaments.models import Golfer
import os
import requests


class Command(BaseCommand):
    help = 'Loads Golfers from ESPN'

    def handle(self, *args, **options):
        self.clear_golfers()
        self.add_players_tournament()
        # self.add_masters_tournament()
        # self.add_pga_tournament()
        # self.add_us_open_tournament()
        # self.add_the_open_tournament()
        self.stdout.write(self.style.SUCCESS('Successfully loaded Golfers'))

    def clear_golfers(self):
        Golfer.objects.all().delete()

    def add_players_tournament(self):
        tournament_url = 'https://www.espn.com/golf/leaderboard?tournamentId=401155428'
        self.get_players(tournament_url)

    def add_masters_tournament(self):
        pass

    def add_pga_tournament(self):
        pass

    def add_us_open_tournament(self):
        pass

    def add_the_open_tournament(self):
        pass

    def get_players(self, tournament_url):
        response = requests.get(tournament_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        field_rows = soup.find_all('a', {'class': 'AnchorLink leaderboard_player_name'})
        for row in field_rows:
            name = row.get_text()
            try:
                Golfer.objects.get(name = name)
            except Golfer.DoesNotExist:
                p = Golfer(name = name)
                p.save()
