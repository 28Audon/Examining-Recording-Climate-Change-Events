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
def index():
    return render_template('base.html')

@app.route('/blank_form.html')
def index():
    return render_template('blank_form.html')

@app.route('/blank.html')
def index():
    return render_template('blank.html')

@app.route('/blog.html')
def index():
    return render_template('blog.html')

@app.route('/blogform.html')
def index():
    return render_template('blogform.html')

@app.route('/blogs.html')
def index():
    return render_template('blogs.html')

@app.route('/commentfrom.html')
def index():
    return render_template('commentfrom.html')