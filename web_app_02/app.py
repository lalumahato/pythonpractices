

from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)

db_name = 'flask_db'
collection = 'user'
# database.create_database(db_name)
# database.create_table(db_name, collection)
@app.route('/')
def home():
  return render_template('home.html')


@app.route('/users', methods=['POST'])
def save_users():
  if request.method == 'POST':
    user  = {
      'name': request.json['name'],
      'email': request.json['email'],
      'phone': request.json['phone'],
      'country': request.json['country'],
    }
  data = database.insert_data(db_name, collection, user)
  return jsonify(data)


@app.route('/users', methods=['GET'])
def find_users():
  if request.method == 'GET':
    data = database.find_all(db_name, collection)
    return data


if __name__ == '__main__':
  app.run(debug=True)
