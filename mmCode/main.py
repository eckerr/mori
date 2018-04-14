# main program to launch Mori Flask app
from app import app, db
import models
import views

from persons.blueprint import persons
app.register_blueprint(persons, url_prefix='/persons')
from cemeteries.blueprint import cemeteries
app.register_blueprint(cemeteries, url_prefix='/cemeteries')

if __name__ == '__main__':
    app.run(debug=true)
