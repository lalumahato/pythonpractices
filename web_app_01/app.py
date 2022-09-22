

import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  port = int(os.getenv('PORT', default=5000))
  app.run(debug=True, port=port)
