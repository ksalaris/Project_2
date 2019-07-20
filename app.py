from flask import Flask, render_template, redirect,current_app
from flask_pymongo import PyMongo
import scrape_flood

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo=PyMongo(app)

@app.route("/")
def home():
    flood_info = mongo.db.flood_info.find_one()

    return render_template("index.html", flood_info=flood_info)

@app.route("/scrape")
def scrape():
    flood_info = mongo.db.flood_info
    flood_data = scrape_flood.scrape_image()
    flood_info.update({}, flood_data, upsert=True)
    
    return redirect("/", code=302)

@app.route("/trends")
def trends():
    return render_template("trends.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about_us.html")

@app.route("/mapIncidence")
def mapIncidence():
    return render_template("incidences_map.html")

@app.route("/fullIncidence")
def fullIncidence():
    return render_template("fullmap_incidences.html")

@app.route("/mapDamage")
def mapDamage():
    return render_template("damage_map.html")

@app.route("/fullDamage")
def fullDamage():
    return render_template("fullmap_damage.html")

@app.route("/data2019")
def data2019():
    return render_template("floodData2019.html")

@app.route("/dataHistorical")
def dataHistorical():
    return render_template("floodsummary.html")

if __name__ == "__main__": 
    app.run(debug= True)