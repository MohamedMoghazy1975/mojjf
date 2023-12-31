import os

from sqlalchemy import create_engine, text

db_connection_string = os.environ['DATABASE_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={
                         "ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                                 }
                       }, pool_pre_ping=True)

def load_courts():
   with engine.connect() as conn:
      result = conn.execute(text("select * from jfdb.Courts"))
      tbcourts = []
   for row in result.all():
          tbcourts.append(row._asdict())
   return tbcourts


def load_court_from_db(id): # /* id is the imput court id */
 with engine.connect() as conn:
   result = conn.execute(text("SELECT * FROM CourtType WHERE CourtID = :val"), {"val": id}
    )
   court = []
   for row in result.all():
         court.append(row._asdict())
   return court

def load_gdwl(id): # /* id is the imput court id */
 with engine.connect() as conn:
   result = conn.execute(text("SELECT * FROM Gdwl WHERE CourtTypeID = :val"), {"val": id}
    )
   gdwl = []
   for row in result.all():
         gdwl.append(row._asdict())
   return gdwl
      
      
def load_basiccase(id): # /* id is the imput court id */
    s = text (
    "SELECT BasicCaseType.* FROM JoinGdwlWBasicCaseType "
    "JOIN BasicCaseType ON JoinGdwlWBasicCaseType.BasicCaseTypeID = " 
    "BasicCaseType.BasicCaseTypeID " 
    "WHERE JoinGdwlWBasicCaseType.GdwlID = :val")
    with engine.connect() as conn:
        result = conn.execute(s, {"val": id})
    basiccase = []
    for row in result.all():
             basiccase.append(row._asdict())
    return basiccase

def load_basiccasetype_from_db(id): # /* id is the imput court id */
 with engine.connect() as conn:
   result = conn.execute(text("SELECT * FROM BasicCaseType WHERE BasicCaseTypeID = :val"), {"val": id}
    )
   specifybasiccase = []
   for row in result.all():
     specifybasiccase.append(row._asdict())
   return specifybasiccase

def load_Requests(id): 
 s = text (
 "SELECT Requests.* FROM JoinBasicCaseTypeRequests "
 "JOIN Requests ON JoinBasicCaseTypeRequests.RequestID = " 
 "Requests.RequestID " 
 "WHERE JoinBasicCaseTypeRequests.BasicCaseTypeID = :val")
 with engine.connect() as conn:
    result = conn.execute(s, {"val": id})
 Requests = []
 for row in result.all():
         Requests.append(row._asdict())
 return Requests