from flask import Flask, jsonify, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://kennymejia10_db_user:G6to5sPxHPp8gBhW@weeklytodo.amcsggs.mongodb.net/?appName=weeklyTODO"
client = MongoClient(MONGODB_URI)

db = client["weeklyTODO"]  # Access the "weeklyTODO" database
collection = db["TODOs"]

app = Flask(__name__)

@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/chores/<day>")
def chores_by_day(day):
    chores = list(collection.find({"day": day}, {"_id": 0}))
    return jsonify(chores)

app.run(host = "0.0.0.0", port=5050)