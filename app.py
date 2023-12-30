from flask import Flask, jsonify, render_template

from database import load_court_from_db, load_courts

app = Flask(__name__)


@app.route("/") 
def hello_world():
  tbcourts = load_courts()
  return render_template('home.html', tbcourts=tbcourts)

@app.route("/api/mydataapi")
def datalist():
  tbcourts = load_courts()
  return jsonify(tbcourts)

@app.route("/court/<id>")
def show_onecourt():
  onecourt = load_court_from_db(id)
  return jsonify(onecourt)
