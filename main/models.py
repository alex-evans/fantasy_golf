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
    tournament_id = models.ForeignKey(Tournament, on_delete = models.CASCADE)
    group_name = models.CharField(max_length = 20)

    class Meta:
        ordering = ['tournament_id', 'group_name']

    def __str__(self):
        return self.tournament_id + ' - ' + self.group_name


class Golfer(models.Model):
    name = models.CharField(max_length = 200)

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
    group_id = models.ForeignKey(Group, on_delete = models.CASCADE)
    golfer_id = models.ForeignKey(Golfer, on_delete = models.CASCADE)

    class Meta:
        ordering = ['group_id', 'golfer_id']

    def __str__(self):
        return self.group_id + ' - ' + self.golfer_id


class MemberPick(models.Model):
    group_golfer_id = models.ForeignKey(GroupGolfer, on_delete = models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete = models.CASCADE)

    class Meta:
        ordering = ['member_id', 'group_golfer_id']

    def __str__(self):
        return self.member_id + ' - ' + self.group_golfer_id
