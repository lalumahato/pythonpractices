from datetime import datetime
from . import db

class User(db.Document):
  name = db.StringField(max_length=30, required=True)
  email = db.EmailField(max_length=40, required=True, unique=True)
  phone = db.StringField(nullable=True, default='')
  country = db.StringField(nullable=True, default='')
  created_at = db.DateTimeField(default=datetime.now) # utcnow

  def to_json(self):
    return {'name': self.name, 'email': self.email}