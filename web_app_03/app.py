from flask import Flask, request, render_template, jsonify
from flask_mongoengine import MongoEngine
from models.student import StudentQuery

# Initialize the app
app = Flask(__name__)

# Connected to database
app.config['MONGODB_SETTING'] = {
  'db': 'flask_db',
  'host': 'localhost',
  'port': 27017
}
db = MongoEngine()
db.init_app(app)


# Default route
@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')


@app.route('/students', methods=['POST'])
def save_user():
  if request.method == 'POST':
    user = {
      'name': request.json['name'], 
      'email': request.json['email'],
    }
    student = StudentQuery.save(user)
    return jsonify(student)


@app.route('/students', methods=['GET'])
def find_users():
  if request.method == 'GET':
    student = StudentQuery.find_all()
    return jsonify(student)


if __name__ == '__main__':
  app.run(debug=True)