from flask import Flask, jsonify, render_template

from database import load_court_from_db, load_courts, load_gdwl

app = Flask(__name__)


@app.route("/") 
def hello_world():
  tbcourts = load_courts()
  return render_template('home.html', tbcourts=tbcourts)

@app.route("/api/mydataapi")
def datalist():
  tbcourts = load_courts()
  return jsonify(tbcourts)

@app.route("/onecourt/<id>") 
def show_onecourt(id):
   court = load_court_from_db(id)
   return jsonify(court)

@app.route("/court/<id>")
def show_onecourtonhtml(id):
  court = load_court_from_db(id)
  return render_template ("court.html", court=court)

@app.route("/gdwl/<id>") 
def show_gdwl(id):
   gdwl = load_gdwl(id)
   return jsonify(gdwl)

@app.route("/gdwal/<id>") 
def specifiy_gdwl(id):
   gdwl = load_gdwl(id)
   return render_template ("gdwal.html", gdwl=gdwl)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
 

