import games
import requests

playoff_game_key = 'P'
allstars_game_key = 'A'

schedules = 'https://statsapi.web.nhl.com/api/v1/schedule'
games_info = 'https://statsapi.web.nhl.com/api/v1/game/'
api_request_timeout = 30


def get_final_game_data(season, game_type):
    season_id = str(int(season) - 1) + str(season)
    payload = {'season': season_id, 'gameType': game_type, 'expand': 'schedule.linescore'}

    dates = requests.get(schedules,
                         params=payload,
                         timeout=api_request_timeout
                        ).json()['dates']


    games_pks = []

    for date in dates:
        date['games'][0]['gamePk']
        games_pks.append(date['games'][0]['gamePk'])

    final_game_game_pk = max(games_pks)

    game_info =  requests.get((games_info + str(final_game_game_pk) + '/feed/live'), 
                                timeout=api_request_timeout).json()['gameData']
    players = game_info['players']
    game_players = []
    for player in players:
            game_players.append(players[player]['fullName'])

    for date in dates:
        if date['games'][0]['gamePk'] == final_game_game_pk:
            home_team = date['games'][0]['teams']['home']['team']['name']
            away_team = date['games'][0]['teams']['away']['team']['name']
            home_team_score = date['games'][0]['teams']['home']['score']
            away_team_score = date['games'][0]['teams']['away']['score']
            players = game_players

            game = games.Game(home_team, 
                              away_team,
                              home_team_score,
                              away_team_score,
                              players)

    return game
