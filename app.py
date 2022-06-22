from flask import Flask
from flask import render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length

app = Flask(__name__)

friend_list = [{"name": "Priya D", "email":"priyad@rvce.du.in" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Priya\'s Friends', friends = friend_list)

@app.route('/priya')
def priya():
    return render_template('priya.html', pageTitle='About Priya')


@app.route('/friend')
def friend():
    return render_template('friend.html', pageTitle='About friend')


@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        email = form['email']
        friend_dict = {"name": fname + " " + lname, "email": email}
        friend_list.append(friend_dict)
        return redirect(url_for('index'))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
