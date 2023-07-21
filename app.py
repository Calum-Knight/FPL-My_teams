from flask import Flask, jsonify, render_template

teams = [
    {"team_name": "On Amad One"},
    {"team_name": "Haa-Haa-Land"}
]

app = Flask(__name__)

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