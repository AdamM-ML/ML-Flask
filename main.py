from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkey1"
app.permanent_session_lifetime = timedelta(minutes=30)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
u_id=0

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    tasks = db.Column(db.String(300))
    def __init__(self, username, tasks):
        self.username=username
        self.tasks=tasks

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/showUsers")
def showUsers():
    return render_template("showUsers.html", values=users.query.all())

@app.route("/deleteUser<u_id>")
def deleteUser(u_id):
    if "username" in session:
        db.session.delete(db.session.query(users).filter(users._id==u_id).first())
        db.session.commit()
        return render_template("showUsers.html", values=users.query.all())
    else:
        flash("you must be logged in to delete users", "info")
        return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        session.permanent = True
        username = request.form["un"]
        session["username"] = username
        username_found = users.query.filter_by(username=username).first()
        if username_found:
            session["tasks"] = username_found.tasks

        else:
            user_n = users(username, "")
            db.session.add(user_n)
            db.session.commit()
        flash("logged in successfully", "info")
        return redirect(url_for("user"))

    else:
        if "username" in session:
            flash("already logged in", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    tasks = None
    if "username" in session:
        username = session["username"]
        if request.method=="POST":
            tasks = request.form.get("tasks")
            session["tasks"] = tasks
            flash("tasks saved")
            username_found = users.query.filter_by(username=username).first()
            username_found.tasks = tasks
            db.session.commit()
        else:
            if "tasks" in session:
                tasks = session["tasks"]
        return render_template("user.html", username=username, tasks=tasks)

    else:
        flash("not logged in", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username", None)
        session.pop("tasks", None)
        flash("logged out successfully", "info")
        return redirect(url_for("login"))
    else:
        flash("you are not logged in", "info")
        return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)



