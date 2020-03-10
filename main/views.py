from django.shortcuts import render


def tournament_view(request):
    tournament = {
    }
    return render(request, 'main/tournament_view.html', tournament)