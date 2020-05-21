from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Reviews, Games
from application.forms import ReviewForm, GameForm, UpdateGameForm


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


@app.route('/game/<int:game_id>')
def game(game_id):
    game = Games.query.get_or_404(game_id)
    return render_template('game.html', title=game.id, game=game)

@app.route('/game/<int:game_id>/update', methods=['GET', 'POST'])
def update_game(game_id):
    game = Games.query.get_or_404(game_id)
    form = UpdateGameForm()
    if form.validate_on_submit():
        game.game_title = form.game_title.data
        game.description = form.description.data
        game.category = form.category.data
        game.age_rating = form.age_rating.data

        db.session.commit()
        return redirect(url_for('game',game_id=game.id))
    elif request.method =='GET':
        form.game_title.data = game.game_title
        form.description.data = game.description
        form.category.data = game.category
        form.age_rating.data = game.age_rating

    return render_template('addgame.html', title='Update Game', form=form)

@app.route('/game/<int:game_id>/delete', methods=['GET','POST'])
def delete_game(game_id):
    game = Games.query.get_or_404(game_id)
    reviews = Reviews.query.filter_by(game_id=game.id).all()
    for review in reviews:
        db.session.delete(review)


    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('games'))




@app.route('/reviews/<int:review_id>')
def reviews(review_id):
    review = Reviews.query.get_or_404(review_id)
    return render_template('review.html', title=review.id, review=review)

@app.route('/reviews/<int:review_id>/update', methods=['GET', 'POST'])
def update_review(review_id):
    review = Reviews.query.get_or_404(review_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review.first_name = form.first_name.data
        review.last_name = form.last_name.data
        review.rating = form.rating.data
        review.title = form.title.data
        review.review = form.review.data

        db.session.commit()
        return redirect(url_for('reviews',review_id=review.id))
    elif request.method =='GET':
        form.first_name.data = review.first_name
        form.last_name.data = review.last_name
        form.rating.data = review.rating
        form.title.data = review.title
        form.review.data = review.review

    return render_template('reviews.html', title='Update Review', form=form)

@app.route('/reviews/<int:review_id>/delete', methods=['GET','POST'])
def delete_review(review_id):
    review = Reviews.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('home'))



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


