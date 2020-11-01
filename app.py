from flask import Flask, render_template
from data import title, subtitle, description, departures, tours

app = Flask(__name__)

###############################################################################
#                              static templates                               #
###############################################################################


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departures_list(departure):
    return render_template('departure.html')


@app.route('/tours/<tour_id>/')
def tours_element(tour_id):
    return render_template('tour.html')


###############################################################################
#                               jinja templates                               #
###############################################################################


@app.route('/data')
def data():

    return render_template('data.html', tours=tours)


@app.route('/data/departures/<departure>')
def data_departures(departure):

    if departure not in departures:
        return 'Такого направления не существует.'

    departure_title = departures[departure]
    departure_tours = {key: value for key, value in tours.items() if value['departure'] == departure}

    return render_template('data-departure.html', departure=departure_title, tours=departure_tours)


@app.route('/data/tours/<tour_id>')
def data_tour(tour_id):

    tour_id = int(tour_id)  # предпочёл бы реализовать в декораторе, но не рискну нарушить тз.

    if tour_id not in tours:
        return 'Такого тура не существует.'

    tour_data = tours[tour_id]

    return render_template('data-tour.html', tour=tour_data)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
