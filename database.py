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
      
      
