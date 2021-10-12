from app import app
from flask import render_template

@app.route('/index')
def index():
    title = "My Main Page"
    return render_template('index.html', title = title)

@app.route('/myfaves')
def myfaves():
    title = "My Favorite Things"
    fav_pasta = ['Penne', 'Rigatoni', 'Bowtie', 'Ravioli', 'Lasagna']
    return render_template('myfaves.html', title = title, fav_pasta = fav_pasta)