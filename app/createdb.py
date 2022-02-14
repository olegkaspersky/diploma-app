import db
import helpers

years = [2021, 2020, 2019]
game_types = ['final', 'allstar']

for game_type in game_types:
    for year in years:
        if game_type == game_types[0]:
            game_info = helpers.get_game_data(helpers.get_season_final(year))

            db.insert_data(game_type, year, game_info)

        elif game_type == game_types[1]:
            if year == 2021:
                continue
            else:
                game_info = helpers.get_game_data(
                    helpers.get_season_allstar_final(year))

                db.insert_data(game_type, year, game_info)
