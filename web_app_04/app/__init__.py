import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv('DB_NAME'),
    'host': os.getenv('HOST'),
    'port': int(os.getenv('DB_PORT'))
}
db = MongoEngine()
db.init_app(app)


from app import views