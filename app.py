from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/about")
def about():

    firstname = "Calum"
    lastname = "Knight"
    location = "home"

    return f"Hello, I'm {firstname} {lastname} and I am at {location}"

hello_dict = {"Hello":"World!"}
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)
    # return hello_dict

@app.route("/normal")
def normal():
    return hello_dict

if __name__ == "__main__":
    app.run(debug=True)