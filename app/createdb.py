import db
import helpers

years = [2021, 2020, 2019, 2018, 2017]
game_types = ['P', 'A']

for game_type in game_types:
    for year in years:
        if year == 2021 and game_type == 'A':
            continue
        else:
            game_info = helpers.get_final_game_data(year, game_type)
            db.insert_data(game_type, year, game_info)
