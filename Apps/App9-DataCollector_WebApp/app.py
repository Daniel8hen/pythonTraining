from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://xiylbmmksczttq:deef5c66e0b3d413b7347ad024ec6cd49d253c31d3cff1f5fa5624cde5359a5a@ec2-107-21-126-193.compute-1.amazonaws.com:5432/d6l41lbcke1h5i?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        #object from Data class
        #first we'll check if there's that email already (since it needs to be unique)
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height)
            count=db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html", text="Email address already exists")


if __name__ == '__main__':
    app.debug=True
    app.run()
