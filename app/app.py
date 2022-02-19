import db
from flask import Flask, render_template, request

app = Flask(__name__)


# @app.before_request
# def start_timer():
#     g.start = time.time()


# @app.after_request
# def after_request(response):
#     timestamp = time.strftime('[%Y-%b-%d %H:%M]')
#     app.logger.error('%s %s %s %s %s %s',
#                      timestamp,
#                      request.remote_addr,
#                      request.method,
#                      request.scheme,
#                      request.full_path,
#                      response.status)
#     return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/final', methods=['GET', 'POST'])
def final():
    if request.method == 'POST':
        year = int(request.form['year'])
        game_data = db.read_data('P', year)
        app.logger.info('User accessed %s final game.', year)
        return render_template('app.html',
                               final=False,
                               home_team=game_data.get_home_team(),
                               away_team=game_data.get_away_team(),
                               home_team_score=game_data.get_home_score(),
                               away_team_score=game_data.get_away_score(),
                               players=game_data.get_game_players()
                               )
    else:
        return render_template('app.html', final=True)


@app.route('/allstar', methods=['GET', 'POST'])
def allstar():
    if request.method == 'POST':
        year = int(request.form['year'])
        app.logger.info('User accessed %s all-star game.', year)
        if year == 2021:
            return render_template('exception.html')
        else:
            game_data = db.read_data('A', year)
            return render_template('app.html',
                                   allstar=False,
                                   home_team=game_data.get_home_team(),
                                   away_team=game_data.get_away_team(),
                                   home_team_score=game_data.get_home_score(),
                                   away_team_score=game_data.get_away_score(),
                                   players=game_data.get_game_players())
    else:
        return render_template('app.html', allstar=True)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('User tried to access not existing page')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.critical('Internal server error')
    return render_template('500.html'), 500
