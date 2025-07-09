from flask import Flask, render_template, url_for, session, redirect
from flask_pymongo import PyMongo
from flask import request, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/User"
mongo = PyMongo(app)

@app.route("/")
def index():
    session["user_id"] = "EMP45678"
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/account")
def account_info():
    if "user_id" not in session:
        return redirect("/")
    user = mongo.db["user information"].find_one({"_id": session["user_id"]})
    return render_template("account.html", user=user)

@app.route("/equipment")
def equipment():
    return render_template("equipment.html")

@app.route("/ticket")
def ticket():
    return render_template("ticket.html")

# --------------------------------------------
# NEW ROUTE: Submit Ticket to 'tickets' collection
# --------------------------------------------
@app.route("/submit_ticket", methods=["POST"])
def submit_ticket():
    if "user_id" not in session:
        return redirect("/")
    print("Form submitted!")

    print("Form data received:")
    print("Equipment:", request.form.get("equipment"))
    print("Model:", request.form.get("model"))
    print("Serial:", request.form.get("serial"))
    print("Issued:", request.form.get("issued"))
    print("Owner:", request.form.get("owner"))
    print("Description:", request.form.get("desc"))

    # Get form data from ticket.html
    ticket_data = {
        "user_id": session["user_id"],
        "equipment": request.form.get("equipment"),
        "model": request.form.get("model"),
        "serial": request.form.get("serial"),
        "issue_date": request.form.get("issued"),
        "owner": request.form.get("owner"),
        "description": request.form.get("desc"),
        "created_at": datetime.utcnow(),
        "status": "Process"
    }

    # Insert into 'tickets' collection in 'User' DB
    mongo.db["tickets"].insert_one(ticket_data)

    flash("✅ Ticket submitted successfully!", "success")
    return redirect("/dashboard")

# --------------------------------------------
# LOGOUT (Optional)
# --------------------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# --------------------------------------------
# Run the app
# --------------------------------------------



if __name__ == "__main__":
    app.run(debug=True)
