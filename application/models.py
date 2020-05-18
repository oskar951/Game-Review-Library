from application import db
from datetime import datetime



class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    review = db.Column(db.String(500), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    game__id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Review: ', str(self.rating), '\r\n', self.title, '\r\n', self.review
            ])




class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    age_rating = db.Column(db.Integer, nullable=False, unique=True)


    def __repr__(self):
        return ''.join([
            'Game: ', str(self.id), '\r\n', self.game_title, '\r\n', self.description,
            'Description: ', self.description, '\r\n', self.category, '\r\n', str(self.age_rating)
            ])
