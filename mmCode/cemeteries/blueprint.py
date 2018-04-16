import os
import pdb
from flask import Blueprint, redirect, url_for, render_template
from flask import request, flash
from werkzeug import secure_filename

from app import app, db
from helpers import object_list
from models import CemeteryEntry, PersonEntry
from cemeteries.forms import CemeteryEntryForm

cemeteries = Blueprint('cemeteries', __name__,
     template_folder='templates')

def get_cemetery_or_404(id):
    query = (CemeteryEntry.query
        .filter(
        (CemeteryEntry.id == id)
        .first_or_404()))
    return query

@cemeteries.route('/')
def index():
    cemeteries = CemeteryEntry.query.order_by(CemeteryEntry.name_of_cemetery)
    return object_list('cemeteries/index.html', cemeteries)

@cemeteries.route('/<id>/')
def detail(id):
    numid = int(id)
    cemetery = CemeteryEntry.query.get(numid)
    return render_template('cemeteries/detail.html', cemetery=cemetery, id=numid)

@cemeteries.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = CemeteryEntryForm(request.form)
        if form.validate():
            cemetery = form.save_cemetery(CemeteryEntry())
            db.session.add(cemetery)
            db.session.commit()
            flash('"%s" entry created successfully.'
                % cemetery.name_of_cemetery, 'success')
            return redirect(url_for('cemeteries.detail', id=cemetery.id))
    else:
        form = CemeteryEntryForm()
    return render_template('cemeteries/create.html', form=form)


@cemeteries.route('/<id>/edit/', methods=['GET', 'POST'])
def edit(id):
    numid = int(id)
    cemetery = CemeteryEntry.query.get(numid)
    if request.method == 'POST':
        form = CemeteryEntryForm(request.form, obj=cemetery)
        if form.validate():
            cemetery = form.save_cemetery(cemetery)
            db.session.add(cemetery)
            db.session.commit()
            flash('"%s" has been edited successfully.' %
                    cemetery.name_of_cemetery, 'success')
            return redirect(url_for('cemeteries.detail',
                id=cemetery.id))
    else:
        form = CemeteryEntryForm(obj=cemetery)
    return render_template('cemeteries/edit.html', cemetery=cemetery,
                form=form)

@cemeteries.route('/<id>/delete/', methods=['GET', 'POST'])
def delete(id):
    # TODO: need to only allow delete if no person records point to this entry
    numid = str(id)
    cemetery = CemeteryEntry.query.get(numid)
    if request.method == 'POST':
        db.session.delete(cemetery)
        db.session.commit()
        flash('Entry "%s" has been deleted successfully.' %
                     cemetery.name_of_cemetery, 'success')
        return redirect(url_for('cemeteries.index'))
    return render_template('cemeteries/delete.html', cemetery=cemetery)
