from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Tournament
import os
import csv


class Command(BaseCommand):
    help = 'Load Projected Tournament Winnings'

    def handle(self, *args, **options):
        players_tournament_obj = Tournament.objects.get(name = 'The PLAYERS Championship')

        os.chdir(os.path.join(os.getcwd(), 'external_files'))
        csv_file_name = 'The PLAYERS Projected Winnings.csv'

        winnings = []
        with open(csv_file_name, encoding = 'utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                winnings.append(row['Projected'])

        players_tournament_obj.projected_winnings = str(winnings)
        players_tournament_obj.save(update_fields = ['projected_winnings'])

        self.stdout.write(self.style.SUCCESS('Successfully loaded projected winnings'))
