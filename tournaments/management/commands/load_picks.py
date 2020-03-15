from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from tournaments.models import Tournament, GroupGolfer, Golfer, Group, Member, MemberPick
import os
import requests
import csv


class Command(BaseCommand):
    help = 'Load Member Tournament Picks'

    def handle(self, *args, **options):
        self.clear_picks()
        players_tournament_obj = Tournament.objects.get(name = 'The PLAYERS Championship')
        os.chdir(os.path.join(os.getcwd(), 'external_files'))
        csv_file_name = 'The PLAYERS Picks.csv'
        group_objs = self.get_groups(players_tournament_obj)

        with open(csv_file_name, encoding = 'utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['Member']:
                    member_name = row['Member']
                
                if row['Group A']:
                    group_a_pick = row['Group A']

                if row['Group B']:
                    group_b_pick = row['Group B']

                if row['Group C']:
                    group_c_pick = row['Group C']

                if row['Group D']:
                    group_d_pick = row['Group D']
                
                self.add_picks(players_tournament_obj, member_name, group_objs, group_a_pick, group_b_pick, group_c_pick, group_d_pick)

        self.stdout.write(self.style.SUCCESS('Successfully loaded Picks'))

    def clear_picks(self):
        MemberPick.objects.all().delete()

    def get_groups(self, tournament_obj):
        return {
            'A': Group.objects.get(tournament = tournament_obj, group_name = 'A'),
            'B': Group.objects.get(tournament = tournament_obj, group_name = 'B'),
            'C': Group.objects.get(tournament = tournament_obj, group_name = 'C'),
            'D': Group.objects.get(tournament = tournament_obj, group_name = 'D'),
        }

    def add_picks(self, tournament_obj, member_name, group_objs, a_pick, b_pick, c_pick, d_pick):
        member_obj = Member.objects.get(name = member_name)
        
        group_golfer_a_obj = self.get_group_golfer(group_objs['A'], a_pick)
        group_golfer_b_obj = self.get_group_golfer(group_objs['B'], b_pick)
        group_golfer_c_obj = self.get_group_golfer(group_objs['C'], c_pick)
        group_golfer_d_obj = self.get_group_golfer(group_objs['D'], d_pick)

        a = MemberPick(
            group_golfer = group_golfer_a_obj,
            member = member_obj
        )
        a.save()

        b = MemberPick(
            group_golfer = group_golfer_b_obj,
            member = member_obj
        )
        b.save()

        c = MemberPick(
            group_golfer = group_golfer_c_obj,
            member = member_obj
        )
        c.save()

        d = MemberPick(
            group_golfer = group_golfer_d_obj,
            member = member_obj
        )
        d.save()

    def get_group_golfer(self, group_obj, golfer_name):
        try:
            golfer = Golfer.objects.get(name = golfer_name)
            return GroupGolfer.objects.get(group = group_obj, golfer = golfer)

        except Golfer.DoesNotExist:
            print(f'ERROR: Golfer does not exist {golfer_name}')

        except GroupGolfer.DoesNotExist:
            print(f'ERROR: GroupGolfer does not exist {group_obj} and {golfer}')
