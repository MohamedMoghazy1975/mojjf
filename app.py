from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, Mohamed Abdel Hafez!</p>"


print(__name__)
if __name__ == "__main__":
  print(" i am inside the if")
  app.run(host='0.0.0.0', port=5000, debug=True)
