from flask import render_template, redirect, url_for
from application import app, db
from application.models import Reviews, Games
from application.forms import ReviewForm, GameForm


@app.route('/')
@app.route('/home')
def home():
    reviewData = Reviews.query.all()
    return render_template('home.html', title="Home Page", reviews=reviewData)



@app.route('/about')
def about():
    return render_template('about.html', title="About Page")


@app.route('/review', methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if  form.validate_on_submit():
        game = Games.query.filter_by(game_title=form.game_title.data).first()
        reviewData = Reviews(
            game_id = game.id,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            rating = form.rating.data,
            title = form.title.data,
            review = form.review.data
            

        )
        db.session.add(reviewData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('reviews.html', title="Game Reviews", form=form)

@app.route('/games')
def games():
    gameData = Games.query.all()
    return render_template('games.html', title="Games Page", games=gameData)

@app.route('/addgame', methods=['GET', 'POST'])
def addgame():

    form = GameForm()
    if form.validate_on_submit():
        gameData = Games(
            game_title = form.game_title.data,
            description = form.description.data,
            category = form.category.data,
            age_rating = form.age_rating.data

        )
        db.session.add(gameData)
        db.session.commit()

        return redirect(url_for('games'))
    else:
        print(form.errors)

    return render_template('addgame.html', title="Add a Game", form=form)


