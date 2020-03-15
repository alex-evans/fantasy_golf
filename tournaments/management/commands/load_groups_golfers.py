from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from tournaments.models import Tournament, GroupGolfer, Golfer, Group
import os
import requests
import csv


class Command(BaseCommand):
    help = 'Load Golfer Groups'

    def handle(self, *args, **options):
        self.clear_groups_golfers()
        players_tournament_obj = Tournament.objects.get(name = 'The PLAYERS Championship')
        os.chdir(os.path.join(os.getcwd(), 'external_files'))
        csv_file_name = 'The PLAYERS Groupings.csv'

        with open(csv_file_name, encoding = 'utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:

                if row['Group A']:
                    golfer_obj = self.get_golfer_obj(row['Group A'])
                    self.add_golfer_to_group(players_tournament_obj, 'A', golfer_obj)

                if row['Group B']:
                    golfer_obj = self.get_golfer_obj(row['Group B'])
                    self.add_golfer_to_group(players_tournament_obj, 'B', golfer_obj)

                if row['Group C']:
                    golfer_obj = self.get_golfer_obj(row['Group C'])
                    self.add_golfer_to_group(players_tournament_obj, 'C', golfer_obj)

                if row['Group D']:
                    golfer_obj = self.get_golfer_obj(row['Group D'])
                    self.add_golfer_to_group(players_tournament_obj, 'D', golfer_obj)

        self.stdout.write(self.style.SUCCESS('Successfully loaded Group Golfers'))

    def clear_groups_golfers(self):
        GroupGolfer.objects.all().delete()

    def get_golfer_obj(self, golfer_name):
        try:
            return Golfer.objects.get(name = golfer_name)
            
        except Golfer.DoesNotExist:
            print(f'ERROR: Golfer does not exist {golfer_name}')

    def add_golfer_to_group(self, tournament_obj, group_ltr, golfer_obj):
        if not golfer_obj:
            return

        try:
            group_obj = Group.objects.get(tournament = tournament_obj, group_name = group_ltr)
            group_golfer = GroupGolfer(
                group = group_obj,
                golfer = golfer_obj
            )
            group_golfer.save()

        except Tournament.DoesNotExist:
            print(f'ERROR: Tournament does not exist {tournament_obj.name}')
