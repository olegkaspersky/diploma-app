import games
from google.cloud import firestore

database = firestore.Client()


def read_data(game_type, season):
    doc_ref = database.collection(game_type).document(str(season))
    db_data = doc_ref.get()
    game = games.Game.from_dict(db_data.to_dict())
    return game


def insert_data(game_type, season, game_info):
    doc_ref = database.collection(game_type).document(str(season))
    doc_ref.set(
        games.Game(game_info.home_team,
                   game_info.away_team,
                   game_info.home_score,
                   game_info.away_score,
                   game_info.players).to_dict())
