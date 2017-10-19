import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def main_page():
  image_names = os.listdir('./static')
  return render_template("main.html", image_names=image_names), 200

@app.route("/eminem")
def eminem_info():

  return render_template("eminem.html", eminem.jpg)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
