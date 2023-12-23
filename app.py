from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'name': 'amin',
  'password': '123'
  },
{
'id': 2,
'name': 'koko',
'password': '123'
  }
]
@app.route("/")
def hello_world():
  return  render_template ('home.html', 
                           jobs=JOBS,
                          mycountry='وزارة العدل')


@app.route("/api/mydataapi")
def datalist():
  return jsonify(JOBS )
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
