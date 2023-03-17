from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
@app.route('/')
def aboutus():
    return render_template('aboutus.html')