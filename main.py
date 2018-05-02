# [START app]
import logging
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import DateField
import datetime

app = Flask(__name__)
app.secret_key = 'SHH!'


class DateForm(FlaskForm):
    dt = DateField('Pick a Date', format="%d/%m/%Y")


@app.route('/', methods=['post','get'])
def home():
    form = DateForm()
    if form.validate_on_submit():
        dob = form.dt.data.strftime('%d/%m/%Y')
        age = datetime.datetime.now()-datetime.datetime(form.dt.data.year,form.dt.data.month,form.dt.data.day)
        return "Your birth date is " + dob + "<br> Your age is " + str(age.days) + " days."
    return render_template('index.html', form=form)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
