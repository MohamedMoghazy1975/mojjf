from flask import Flask, jsonify, render_template

from database import load_courts

app = Flask(__name__)


@app.route("/")
def hello_world():
    tbcourts = load_courts()
    return render_template('home.html', tbcourts=tbcourts)

@app.route("/api/mydataapi")
def datalist():
    tbcourts = load_courts()
    return jsonify(tbcourts)


  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
