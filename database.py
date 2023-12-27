from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://kgv1bkvwio96ojtzy0dz:pscale_pw_RowBV41gt9wIhn9o1Lg4bP013qz5z0VyLcUhhpbifUv@aws.connect.psdb.cloud/jfdb?charset=utf8mb4" 

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
