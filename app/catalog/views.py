# -*- coding: utf-8 -*-
#from flask import request, Blueprint, render_template, \
#    redirect, url_for
from flask import request, Blueprint, render_template, json, jsonify, flash, \
    redirect, url_for, send_from_directory, config, session, Response
import sys
from app import app, db, manager, admin
from app.catalog.models import Data, DataForm
from flask_admin.contrib.sqla import ModelView

reload(sys)
sys.setdefaultencoding("utf-8")

catalog = Blueprint('catalog', __name__)

manager.create_api(Data, methods=['GET','POST'], results_per_page=None)

admin.add_view(ModelView(Data, db.session))

@catalog.route('/data', methods=['GET', 'POST'])
def data():
    form = DataForm(request.form)

    choices = []
    for size in range(35, 50, 1):  # filled clothe size range 35 to 49
        choices.append((str(size), (str(size))))
    form.foot_size.choices = choices

    choices = []
    for size in range(32, 69, 2):  # filled clothe size range 32 to 68
        choices.append((str(size), (str(size))))
    form.cloth_size.choices = choices

    if request.method == 'POST':
        name = form.name.data
        password = form.password.data



        flash('name: [%s]' % name, 'success')
        return redirect(url_for('catalog.data'))

    return render_template('data.html', form=form)

