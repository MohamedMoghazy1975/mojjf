from flask import Flask, jsonify, render_template, request, session, redirect

from database import load_Requests, load_basiccase, load_court_from_db, load_courts, load_gdwl, load_basiccasetype_from_db



app = Flask(__name__)
app.secret_key = "1234567891011121314151617181920"


# this route to home.html and load all courts data and show it in the home page
# all data in tbcourts variable the variable is a jsonify to /api/mydataapi
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
  session['C_ID'] = (id)
  return render_template ("court.html", court=court)

@app.route("/gdwl/<id>") 
def show_gdwl(id):
   gdwl = load_gdwl(id)
   return jsonify(gdwl)

@app.route("/gdwal/<id>") 
def specifiy_gdwl(id):
   gdwl = load_gdwl(id)
   session['C_Type'] = (id)
   return render_template ("gdwal.html", gdwl=gdwl)

@app.route("/basiccasej/<id>") 
def show_basiccases(id):
   basiccase = load_basiccase(id)
   return jsonify(basiccase)

@app.route("/basiccasetype/<id>") 
def specifiy_basiccase(id):
   basiccase = load_basiccase(id)
   session['C_G'] = (id)
   return render_template ("basiccasetype.html", basiccase=basiccase )

@app.route("/basiccasej2/<id>") 
def req_basiccases(id):
   specifybasiccase = load_basiccasetype_from_db(id)
   return jsonify(specifybasiccase)

@app.route("/allrequests/<id>") 
def basic_request(id):
   myrequests = load_Requests(id)
   return jsonify(myrequests)

@app.route("/request/<id>") 
def show_requests(id):
   myrequests1 = load_Requests(id)
   specifybasiccase = load_basiccasetype_from_db(id)
   variable_to_pass = (id)
   return render_template ("request.html", myrequests1=myrequests1,
                          variable_to_pass=variable_to_pass
                          ,specifybasiccase=specifybasiccase
                         )

@app.route("/court/<id>/apply")
def appl_req(id):
   data=request.args
   return jsonify(data)  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
 

