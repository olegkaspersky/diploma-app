import games
import requests

schedules = 'https://statsapi.web.nhl.com/api/v1/schedule'
games_info = 'https://statsapi.web.nhl.com/api/v1/game/'
api_request_timeout = 30

playoff_game_key = 'P'
allstars_game_key = 'A'


def get_season_final(season):
    season_id = str(int(season) - 1) + str(season)
    payload = {'season': season_id, 'gameType': 'P'}

    playoffs_games_data = requests.get(schedules,
                                       params=payload,
                                       timeout=api_request_timeout
                                       ).json()

    dates = playoffs_games_data['dates']

    games_pks = []

    for date in dates:
        for game in date['games']:
            games_pks.append(game['gamePk'])

    final_game_pk = str(max(games_pks))

    return final_game_pk


def get_season_allstar_final(season):
    season_id = str(int(season) - 1) + str(season)
    payload = {'season': season_id, 'gameType': 'A'}
    allstar_games_data = requests.get(schedules,
                                      params=payload,
                                      timeout=api_request_timeout
                                      ).json()

    dates = allstar_games_data['dates']

    games_pks = []

    for date in dates:
        for game in date['games']:
            games_pks.append(game['gamePk'])

    allstar_final_game_pk = str(max(games_pks))

    return allstar_final_game_pk


def get_game_data(game_pk):
    game_info = requests.get((games_info + str(game_pk) + '/feed/live'),
                             timeout=api_request_timeout
                             ).json()['gameData']

    schedule = requests.get(schedules,
                            params={'gamePk': game_pk},
                            timeout=api_request_timeout
                            ).json()

    home_team = game_info['teams']['home']['name']
    away_team = game_info['teams']['away']['name']

    home_score = schedule['dates'][0]['games'][0]['teams']['home']['score']
    away_score = schedule['dates'][0]['games'][0]['teams']['away']['score']

    players = game_info['players']
    game_players = []
    for player in players:
        game_players.append(players[player]['fullName'])

    game = games.Game(home_team=home_team,
                      away_team=away_team,
                      home_score=home_score,
                      away_score=away_score,
                      players=game_players
                      )

    return game
