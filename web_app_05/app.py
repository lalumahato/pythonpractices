
from flask import Flask, redirect, url_for, request, render_template, make_response
from flask import abort
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message


app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/admin')
def admin():
  return '<h1>Hello Admin</h1>'

@app.route('/admin/<guest>')
def guest(guest):
  return 'Hello %s as guest' % guest


@app.route('/user/<name>')
def user(name):
  if name == 'admin':
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('guest', guest=name))


@app.route('/welcome/<name>')
def welcome(name):
  return 'Welcome %s' % name


@app.route('/login_user', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = request.form['nm']
    return redirect(url_for('welcome', name=user))
  else:
    user = request.args.get('nm')
    return redirect(url_for('welcome', name=user))


# Read data from FORM and Display 
@app.route('/student', methods=['GET'])
def student():
  return render_template('student.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST':
    result = request.form
    return render_template('result.html', result=result)


# Set Cookie
@app.route('/cookie')
def cookie():
  return render_template('cookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def set_cookie():
  if request.method == 'POST':
    user = request.form['name']
    response = make_response(render_template('setcookie.html')) 
    response.set_cookie('user', user)
    return response


@app.route('/getcookie', methods=['POST', 'GET'])
def get_cookie():
  if request.method == 'GET':
    cookie = request.cookies.get('user')
    return f'Hello, {cookie}'


# Login 
@app.route('/login')
def login_home():
  return render_template('login.html')


@app.route('/get_login', methods=['POST', 'GET'])
def get_login():
  if request.method == 'POST':
    username = request.form['name']
    if username == 'admin':
      return redirect(url_for('success'))
    else:
      abort(401)
  else:
    return redirect(url_for('get_login'))

@app.route('/success')
def success():
  return '<h3>Logged in successfully.</h3>'


# File Upload
@app.route('/upload')
def file_upload():
  return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def file_uploader():
  if request.method == 'POST':
    file = request.files['file']
    file.save(secure_filename(file.filename))
    return 'File uploaded successfully.' 


# Mail
sender_email = 'lalu.mahato@weboniselab.com'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender_email
app.config['MAIL_PASSWORD'] = 'qelxrsyepbmfiraz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)

@app.route('/send_mail')
def send_email():
  message = Message('Hello', sender=sender_email, recipients=['testcbiu@yopmail.com'])
  message.body = 'Hello, This is a sample mail to test flask email service.'
  mail.send(message)
  return 'Email Sent'

if __name__ == '__main__':
  app.run(debug=True)
