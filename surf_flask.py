from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.surf_summaryDB
collection = db.surf_summary


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a var
    inventory = list(db.surf_summary.find())
    print(inventory)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", inventory=inventory)


if __name__ == "__main__":
    app.run(debug=True)
