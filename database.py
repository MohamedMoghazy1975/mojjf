from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://dnmb9e6yflhuoh7s3e5f:pscale_pw_QhjXlL83Gyg886MofW0G9Mwf8v3jjXcpa2gqxTTGP72@aws.connect.psdb.cloud/jfdb?charset=utf8mb4" 

engine = create_engine(db_connection_string,
                       connect_args={
                         "ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                                 }
                       })

def load_courts():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jfdb.Courts"))
      tbcourts = []
      for row in result.all():
          tbcourts.append(row._asdict())
      return tbcourts
