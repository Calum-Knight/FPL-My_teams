from flask import Flask, jsonify, render_template
import pymongo

app = Flask(__name__)

#Connect to database
conn = "mongobd://localhost:27017"
client = pymongo.MongoClient(conn)

#connect to collection (if using MongoDB)
db = client.DBNAME
user_defined_variable = db.COLLECTIONNAME

#teams list will not be needed once connected to DB
teams = [
    {"team_name": "On Amad One"},
    {"team_name": "Haa-Haa-Land"}
]



@app.route("/")
def index():
    return render_template("index.html", text = "Card to display captain details")

@app.route("/home")
def home():
    return render_template("index.html", text = "Card to display captain details")

@app.route("/<team_name>")
def team_data(team_name):
    canonicalized = team_name.replace(" ", "").lower()
    for team in teams:
        search_term = team["team_name"].replace(" ", "").lower()

        if search_term == canonicalized:
            return render_template("team_details.html", team_name = team["team_name"])

    return jsonify({"error": f"Character with real_name {team_name} not found."}), 404



if __name__ == "__main__":
    app.run(debug=True)