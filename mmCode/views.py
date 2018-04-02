# views.py   for Mori Flask app
from app import app
from flask import render_template, request

@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('homepage.html', name=name, number=number)

@app.route('/r')
def responsive():
    return render_template('resp.html')

@app.route('/s')
def show_individuals():
    C = """Clarence Francis Kerr was born on Wednesday, August, 28, 1929. He \
    died on Thursday, December, 23, 2004 at the age of 75.\
    It has been 13 years since his death. If he were alive today, \
    he would be 88 years old."""
    M = """Marion Elaine Kerr was born on Thursday, April, 09, 1931. She died \
    on Monday, June, 03, 1991 at the age of 60. \
    It has been 26 years since her death. If she were alive today, \
    she would be 87 years old."""
    mlist = [('Marion Elaine Kerr', 'marion80x80.png', M),
            ('Clarence Francis Kerr', 'clarence80x80.png', C)]

    return render_template('show_individual.html', mlist=mlist)
