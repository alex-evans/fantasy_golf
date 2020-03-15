from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length = 200)
    # start_date = models.DateField('start date')
    # end_date = models.DateField('end date')
    # leaderboard_url = models.CharField(max_length=200, blank=True)
    # course = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Group(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete = models.CASCADE)
    group_name = models.CharField(max_length = 20)

    class Meta:
        ordering = ['tournament', 'group_name']

    def __str__(self):
        return str(self.tournament) + ' - ' + self.group_name


class Golfer(models.Model):
    name = models.CharField(max_length = 200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class GroupGolfer(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    golfer = models.ForeignKey(Golfer, on_delete = models.CASCADE)

    class Meta:
        ordering = ['group', 'golfer']

    def __str__(self):
        return self.group.tournament.name + '-' + self.group.group_name + ' - ' + self.golfer.name


class MemberPick(models.Model):
    group_golfer = models.ForeignKey(GroupGolfer, on_delete = models.CASCADE)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)

    class Meta:
        ordering = ['member', 'group_golfer']

    def __str__(self):
        return self.member.name + ' - ' + self.group_golfer.group.tournament.name + ' - ' + self.group_golfer.group.group_name + ' - ' + self.group_golfer.golfer.name
