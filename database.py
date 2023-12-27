from sqlalchemy import create_engine, text
import os

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
