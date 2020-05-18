from flask import render_template
from application import app



@app.route('/')
@app.route('/home')
def home():
    reviewData = Reviews.query.all()
    return render_template('home.html', title="Home Page", review=reviewData)



@app.route('/about')
def about():
    return render_template('about.html', title="About Page")


@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title="Game Reviews")

@app.route('/games')
def games():
    return render_template('games.html', title="Games Page")



