import os
from flask import Blueprint, redirect, url_for, render_template
from flask import request, flash
from werkzeug import secure_filename

from app import app, db
from helpers import object_list
from models import CemeteryEntry, PersonEntry
from persons.forms import PersonEntryForm
from create_stats import create_stats, get_stats, str_to_date

persons = Blueprint('persons', __name__,
template_folder='templates')

@persons.route('/')
def index():
    #persons = PersonEntry.query.order_by(PersonEntry.last_name, PersonEntry.first_name)
    #persons = PersonEntry.query.join(CemeteryEntry,
    #        CemeteryEntry.id==PersonEntry.cemetery_id).\
    #    order_by(PersonEntry.last_name, PersonEntry.first_name)
    #pdb
    persons = db.session.query(PersonEntry, CemeteryEntry).\
            filter(CemeteryEntry.id==PersonEntry.cemetery_id).\
            order_by(PersonEntry.last_name, PersonEntry.first_name)
    return object_list('persons/index.html', persons)
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

@persons.route('/<id>/')
def detail(id):
    numid = int(id)
    person = PersonEntry.query.get(numid)
    #if (person.day_of_birth_known and person.month_of_birth_known and person.year_of_birth_known):
    #    birth_death, time_past = create_stats(person)
    #else: birth_death, time_past = '', ''
    birth_death, time_past = '', ''
    birth_death = " ".join(birth_death)
    time_past = " ".join(time_past)
    cemetery = CemeteryEntry.query.get(person.cemetery_id)
    return render_template('persons/detail.html', person=person, id=numid,
                 cemetery=cemetery, birth_death=birth_death, time_past=time_past)

@persons.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = PersonEntryForm(request.form)
        if form.validate():
            person = form.save_person(PersonEntry())
            db.session.add(person)
            db.session.commit()
            flash('"%s", "%s", "%s" entry created successfully.'
                % (person.first_name, person.middle_name, person.last_name),
                'success')
            return redirect(url_for('persons.detail', id=person.id))
    else:
        form = PersonEntryForm()
    return render_template('persons/create.html', form=form)

@persons.route('/<id>/edit/', methods=['GET', 'POST'])
def edit(id):
    numid = int(id)
    person = PersonEntry.query.get(numid)
    form = PersonEntryForm(request.form, obj=person)
    if request.method == 'POST':
        form = PersonEntryForm(request.form, obj=person)
        if form.validate():
            person = form.save_person(person)
            db.session.add(person)
            db.session.commit()
            flash('"%s", "%s", "%s" entry edited successfully.'
                % (person.first_name, person.middle_name, person.last_name),
                'success')
            return redirect(url_for('persons.detail', id=id))
    else:
        form = PersonEntryForm(obj=person)
    return render_template('persons/edit.html', person=person, form=form)

@persons.route('/<id>/delete/', methods=['GET', 'POST'])
def delete(id):
    numid = str(id)
    person = PersonEntry.query.get(numid)
    if request.method == 'POST':
        db.session.delete(person)
        db.session.commit()
        flash('Entry for "%s" has been deleted successfully.' %
           (person.first_name + ' '+ person.middle_name + ' ' +
             person.last_name), 'success')
        return redirect(url_for('persons.index'))
    return render_template('persons/delete.html', person=person)
