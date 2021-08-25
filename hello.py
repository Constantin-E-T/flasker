from flask import Flask, render_template, flash
from flask.templating import render_template
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Filters

'''
safe
capitalize
lower
upper
title
trim
striptags
'''

# Create a Flask Instance
app = Flask(__name__) 
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

# Create a form class

class NamerForm(FlaskForm):
 name = StringField("What's Your Name", validators=[DataRequired()])
 submit = SubmitField("Submit")

# Create a route decorator

@app.route('/')

#def index():
# return "<h1>Hello World!</h1>"
def index():
 return render_template("index.html")

# Localhost:5000/user/Emilian

@app.route('/user/<name>')

def user(name):
 return render_template("user.html", user_name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_fund(e):
 return render_template("404.html"), 404

# Internal server error 
@app.errorhandler(500)
def page_not_fund(e):
 return render_template("500.html"), 500

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
 name = None
 form = NamerForm()
 # Validate Form
 if form.validate_on_submit():
     name = form.name.data
     form.name.data =  ''
     flash("Form Submited Succesfully")

 return render_template("name.html",
     name = name,
     form = form
 )