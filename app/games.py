class Game(object):
    def __init__(self,
                 home_team,
                 away_team,
                 home_score,
                 away_score,
                 players):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.players = players

    def get_home_team(self):
        return self.home_team

    def get_away_team(self):
        return self.away_team

    def get_home_score(self):
        return self.home_score

    def get_away_score(self):
        return self.away_score

    def get_game_players(self):
        return self.players

    @staticmethod
    def from_dict(source):
        game = Game(source[u'home_team'],
                    source[u'away_team'],
                    source[u'home_score'],
                    source[u'away_score'],
                    source[u'players'])

        if u'home_team' in source:
            game.home_team = source[u'home_team']

        if u'away_team' in source:
            game.away_team = source[u'away_team']

        if u'home_score' in source:
            game.home_score = source[u'home_score']

        if u'away_score' in source:
            game.away_score = source[u'away_score']

        if u'players' in source:
            game.players = source[u'players']

        return game

    def to_dict(self):
        dest = {
            u'home_team': self.home_team,
            u'away_team': self.away_team,
            u'home_score': self.home_score,
            u'away_score': self.away_score,
            u'players': self.players
        }

        if self.home_team:
            dest[u'home_team'] = self.home_team

        if self.away_team:
            dest[u'away_team'] = self.away_team

        if self.home_score:
            dest[u'home_score'] = self.home_score

        if self.away_score:
            dest[u'away_score'] = self.away_score

        if self.players:
            dest[u'players'] = self.players

        return dest

    def __repr__(self):
        """Return game information in string format."""
        return(
            f'Game(\
                home_team={self.home_team}, \
                away_team={self.away_team}, \
                home_score={self.home_score}, \
                away_score={self.away_score}, \
                players={self.players}\
            )'
        )
