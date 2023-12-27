from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://t9748cv1jtxrwodf7iis:pscale_pw_Ltbf3VouFealCgkjzSNTc9SO0sgO1xK8U6cJ0fk0jDU@aws.connect.psdb.cloud/jfdb?charset=utf8mb4" 

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
