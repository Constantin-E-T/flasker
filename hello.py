from flask import Flask, render_template
from flask.templating import render_template

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