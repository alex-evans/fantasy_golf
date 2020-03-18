from bs4 import BeautifulSoup
import os
import requests


def get_positions():
    leaderboard = {}
    position_count = {}

    # First Get the Leaderboard
    leaderboard_url = 'https://www.pga.com/events/leaderboards/pga-tour'
    response = requests.get(leaderboard_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    leaderboard_rows = soup.find_all('div', {'class': 'jss286'})
    for row in leaderboard_rows:
        position = row.find('div', {'class': 'jss289'}).text
        golfer = row.find('div', {'class': 'jss290'})['data-gtm-player-name']

        leaderboard[golfer] = position

    # Then determine how many ties for each position to help with determining winnings
    for golfer, pos in leaderboard.items():
        if pos in position_count:
            position_count[pos] += 1
        else:
            position_count[pos] = 1

    return leaderboard, position_count     