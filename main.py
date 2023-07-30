from flask import Flask, render_template, request
from functions import *

app = Flask('Flask App', static_folder='static', template_folder="templates")

@app.route('/', methods=["GET", "POST"])
def home():
  return render_template('index.html')

app.run(host='0.0.0.0', port=6969, threaded=True)