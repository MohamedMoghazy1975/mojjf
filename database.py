from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://jh25a7v1lav81kiq8mou:pscale_pw_NfelX8ScIPXaEpZpfnMfKjK1BZPjxDAoe6xkUzWpCfQ@aws.connect.psdb.cloud/jfdb?charset=utf8mb4"

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
