import mysql.connector
# connection = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='flight_1',
#          user='root',
#          password='rahelehz',
#          autocommit=True
#          )
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLAlchemy_host"]='127.0.0.1',
app.config["SQLAlchemy_port"]=3306,
app.config["SQLAlchemy_user"]='root',
app.config["SQLAlchemy_password"]='rahelehz',
app.config["SQLAlchemy_db"]='flight_1'
mysql=SQLAlchemy(app)

@app.route('/')
def index():
    args = request.args
    ICAO = int(args.get("ICAO"))
    sql="Select name,location From airport where gps_code='"+ICAO+"'"
    cursor=mysql.connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        nameAirport=row[0]
        location=row[1]

    response = {
        "ICAO":ICAO,
        "Name":nameAirport,
        "Location":location
    }

    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)