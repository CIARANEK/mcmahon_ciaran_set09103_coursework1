import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def main_page():
  image_names = os.listdir('./static')
  return render_template("main.html", image_names=image_names), 200

@app.route("/eminem.jpg")
def eminem_info():
  filename = url_for('static' , filename='eminem.jpg')
  return render_template("eminem.html", filename=filename)
  
@app.route("/fleetwood.jpg")
def fleetwood_info():
  filename = url_for('static' , filename='fleetwood.jpg')
  return render_template("fleetwood.html", filename=filename)

@app.route("/marvin.jpg")
def marvin_info():
  filename = url_for('static' , filename='marvin.jpg')
  return render_template("marvin.html", filename=filename)
  
@app.route("/jackson.jpg")
def jackson_info():
  filename = url_for('static' , filename='jackson.jpg')
  return render_template("jackson.html", filename=filename)
  
@app.route("/elvis.jpg")
def elvis_info():
  filename = url_for('static' , filename='elvis.jpg')
  return render_template("elvis.html", filename=filename)

@app.route("/aerosmith.jpg")
def aerosmith_info():
  filename = url_for('static' , filename='aerosmith.jpg')
  return render_template("aerosmith.html", filename=filename)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
