import pyshorteners

from flask import redirect, render_template, request, flash, url_for
from flask_app import app

# Home | Main page
@app.route('/')
def index():
    return render_template('index.html')

# Create short URL with form
@app.route('/create_shorturl', methods=['POST'])
def create_shorturl():
    # print(request.form)
    long_url = request.form.get('long_url')
    if long_url:
        # print to confirm long_url is being passed
        # print(long_url) 
        short = pyshorteners.Shortener()
        try:
            short_url = short.tinyurl.short(long_url)
            # print to confirm short_url is being passed
            # print(short_url)
            flash(short_url, 'success')
        except Exception as e:
            print(e)
            flash('An error ocurred, please try again', 'error')
    else:
        flash('Please enter a URL.', 'error')
    return redirect(url_for('index'))

# About this proyect
@app.route('/about_this')
def view_about_this():
    return render_template('about_this.html')