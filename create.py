from application import db
from application.models import Reviews, Games

db.drop_all()
db.create_all()
