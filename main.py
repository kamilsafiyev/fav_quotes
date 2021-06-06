from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+psycopg2://postgres:root@localhost/quotes"
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://eltzpyzyevkqti:20513bca186c47fecf0b619484d8df4276ded201ac0c7a3b02a9ef57065d0f21@ec2-34-255-134-200.eu-west-1.compute.amazonaws.com:5432/dfmpe9a55sq2n8"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    quote = db.Column(db.String(230))



@app.route("/")
def index():
    result=Favquotes.query.all()
    return render_template("index.html",result=result)

@app.route("/quotes")
def quotes():
    return render_template("quote.html")


@app.route("/process",methods=["POST"])
def process():
    author=request.form["author"]
    quote=request.form["quote"]
    signature=Favquotes(author=author,quote=quote)
    db.session.add(signature)
    db.session.commit()
    
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run()

