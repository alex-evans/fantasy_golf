from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Member
import os


class Command(BaseCommand):
    help = 'Loads Golfers from ESPN'

    def handle(self, *args, **options):
        self.clear_members()
        members = [
            'Alex',
            'Andy',
            'Brad',
            'Brandon',
            'David',
            'Joel',
            'John',
            'Kevin',
            'Rey',
            'Rick',
            'Ryan',
        ]
        self.stdout.write(self.style.SUCCESS('Successfully loaded Members'))

        for member_name in members:
            m = Member(name = member_name)
            m.save()

    def clear_members(self):
        Member.objects.all().delete()
