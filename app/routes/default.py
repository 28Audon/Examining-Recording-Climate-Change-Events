from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

# Other
@app.route('/base.html')
def base():
    return render_template('base.html')

@app.route('/blank_form.html')
def blank_form():
    return render_template('blank_form.html')

@app.route('/blank.html')
def blank():
    return render_template('blank.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/blogform.html')
def blogform():
    return render_template('blogform.html')

@app.route('/blogs.html')
def blogs():
    return render_template('blogs.html')

@app.route('/commentfrom.html')
def commentfrom():
    return render_template('commentfrom.html')

@app.route('/profileform.html')
def profileform():
    return render_template('profileform.html')

@app.route('/profilemy.html')
def profilemy():
    return render_template('profilemy.html')