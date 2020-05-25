import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Games, Reviews
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        game = Games(game_title = 'GTA V', description = 'Gangs', category = 'Action', age_rating = '18')
        # save data to database
        db.session.add(game)
        db.session.commit()
        review = Reviews(first_name = 'oskar', last_name = 'ceremnovas', rating = '5', title = 'review', review = 'good')
        db.session.add(review)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_view(self):
        response=self.client.get(url_for('home'))

        self.assertEqual(response.status_code,200)


    def test_about_view(self):
        response=self.client.get(url_for('about'))

        self.assertEqual(response.status_code,200)

    def test_addgame_view(self):
        response=self.client.get(url_for('addgame'))

        self.assertEqual(response.status_code,200)
    
    def test_games_view(self):
        response=self.client.get(url_for('games'))

        self.assertEqual(response.status_code,200)

    def test_reviews_view(self):
        response=self.client.get(url_for('review'))

        self.assertEqual(response.status_code,200)




class TestModels(TestBase):
    def test_game_validation(self):
        response=self.client.post(
            '/addgame',
            data=dict(
            game_title = 'GTA V', 
            description = 'Gangs', 
            category = 'Action', 
            age_rating = '19'



            ),
            follow_redirects=True
        )
        self.assertIn(b'18 years is the max age rating', response.data)


    


    def test_review_validation(self):
        response=self.client.post(
            '/review',
            data=dict(
            first_name = 'oskar', 
            last_name = 'ceremnovas', 
            rating = '11', 
            title = 'review', 
            review = 'good'



            ),
            follow_redirects=True
        )
        self.assertIn(b'Rating must be between 1 - 10', response.data)





    def test_repr(self):
         game = Games(game_title = 'GTA V', description = 'Gangs', category = 'Action', age_rating = '18')
         print(repr(game))
         review = Reviews(first_name = 'oskar', last_name = 'ceremnovas', rating = '5', title = 'review', review = 'good')
         print(repr(review))






class TestPosts(TestBase):
    def test_add_new_game(self):
        response=self.client.post(
            '/addgame',
            data=dict(
            game_title = 'GTA V', 
            description = 'Gangs', 
            category = 'Action', 
            age_rating = '18'

            ),
            follow_redirects=True
        )
        self.assertIn(b'Add a Game', response.data)
        with self.client:
            response=self.client.get(url_for('game',game_id=1))
            self.assertEqual(response.status_code,200)

            
        
        with self.client:
            response=self.client.get(url_for('update_game', game_id=1))
            self.assertEqual(response.status_code,200)
            response=self.client.post(
                '/game/1/update',
                data=dict(
                game_title = 'GTA V', 
                description = 'Criminals', 
                category = 'Action', 
                age_rating = '18'
                ),
                follow_redirects=True
            )
            self.assertIn(b'1', response.data)



        with self.client:
            response=self.client.get(url_for('update_game', game_id=1))
            self.assertEqual(response.status_code,200)
            response=self.client.post(
                '/game/1/update',
                data=dict(
                game_title = 'GTA V', 
                description = 'Criminals', 
                category = 'Action', 
                age_rating = '19'
                ),
                follow_redirects=True
            )
            self.assertIn(b'18 years is the max age rating', response.data)
        
        with self.client:
            response=self.client.post(
                '/review',
                data=dict(
                    first_name = 'oskar', 
                    last_name = 'ceremnovas', 
                    rating = '5', 
                    title = 'review', 
                    review = 'good'
                ),
                follow_redirects=True
            )
            self.assertIn(b'Game Reviews', response.data)
        
        with self.client:
            response=self.client.get(url_for('reviews', review_id=1))
            self.assertEqual(response.status_code,200)


        
        
        with self.client:
            response=self.client.get(url_for('update_review', review_id=1))
            self.assertEqual(response.status_code,200)
            response=self.client.post(
                '/reviews/1/update',
                data=dict(
                    first_name = 'oskar', 
                    last_name = 'ceremnovas', 
                    rating = '5', 
                    title = 'review', 
                    review = 'alright'
                ),
                follow_redirects=True
            )
            self.assertIn(b'1', response.data)

            
        
        with self.client:
            response=self.client.get(url_for('delete_review', review_id=1))
            self.assertEqual(response.status_code,302)

        with self.client:
            response=self.client.get(url_for('delete_game', game_id=1))
            self.assertEqual(response.status_code,302)

