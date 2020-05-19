from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from application.models import Games, Reviews

class ReviewForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    game_title = StringField('Game Title',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    
    )


    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    rating = IntegerField('Rating',
        validators = [
            DataRequired(),
            
        ]
    )


    review = StringField('Review',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post')


    def validate_rating(self,rating):
        if rating.data > 10:
            raise ValidationError('Rating must be between 1 - 10')




class GameForm(FlaskForm):
    game_title = StringField('Game Title',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    description = StringField('Description',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )


    category = StringField('Category',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    age_rating = IntegerField('Age Rating',
        validators = [
            DataRequired(),
           
        ]
    )

    submit = SubmitField('Add')

    def validate_age_rating(self,age_rating):
        if age_rating.data > 18:
            raise ValidationError('18 years is the max age rating')


    def validate_game_title(self,game_title):
        game = Games.query.filter_by(game_title=game_title.data).first()

        if game:
            raise ValidationError('Game already exists')

