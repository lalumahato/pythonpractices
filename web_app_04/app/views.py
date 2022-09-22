from app import app
from flask import render_template, request, jsonify
from .models import User


@app.route('/')
def index():
  user = { 'username': 'Flask'}
  posts = [
    {'author': {'name': 'Peter Parker'},'body': 'Movie was amazing.'},
    {'author': {'name': 'John Conner'},'body': 'I like sci-fi stuff.'},
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/users', methods=['POST'])
def save_user():
  if request.method == 'POST':
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    country = request.json['country']
  user = User(name=name, email=email, phone=phone, country=country)
  data = user.save()
  return jsonify(data)

@app.route('/users', methods=['GET'])
def find_users():
  if request.method == 'GET':
    users = User.objects().order_by('-created_at')
    return jsonify(users)

