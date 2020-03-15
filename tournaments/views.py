from django.shortcuts import render
from tournaments.models import Tournament, Golfer, GroupGolfer, Member, MemberPick


def get_golfers(picks):

    golfer_a = ''
    golfer_b = ''
    golfer_c = ''
    golfer_d = ''

    for pick in picks:
        group_golfer = pick.group_golfer
        group = group_golfer.group
        spot = group.group_name
        golfer = group_golfer.golfer
        if spot == 'A':
            golfer_a = golfer
        if spot == 'B':
            golfer_b = golfer
        if spot == 'C':
            golfer_c = golfer
        if spot == 'D':
            golfer_d = golfer

    return golfer_a, golfer_b, golfer_c, golfer_d


def get_winnings(golfer):
    return 0


def get_tournament_obj():
    players_tournament_obj = Tournament.objects.get(name = 'The PLAYERS Championship')
    members = Member.objects.all()

    members_info = []

    for member in members:
        member_picks = MemberPick.objects.filter(member = member)
        
        pick_a, pick_b, pick_c, pick_d = get_golfers(member_picks)

        pick_a_winnings = get_winnings(pick_a)
        pick_b_winnings = get_winnings(pick_b)
        pick_c_winnings = get_winnings(pick_c)
        pick_d_winnings = get_winnings(pick_d)

        total_winnings = pick_a_winnings + pick_b_winnings + pick_c_winnings + pick_d_winnings

        info = {
            'name': member.name,
            'pick_a': pick_a,
            'pick_a_winnings': pick_a_winnings,
            'pick_b': pick_b,
            'pick_b_winnings': pick_b_winnings,
            'pick_c': pick_c,
            'pick_c_winnings': pick_c_winnings,
            'pick_d': pick_d,
            'pick_d_winnings': pick_d_winnings,
            'total': total_winnings
        }

        members_info.append(info)

        
    return {
        'members': members_info
    }

def tournament_view(request):

    tournament = get_tournament_obj()

    return render(request, 'tournaments/tournament_view.html', tournament)