from flask import Flask, render_template,request
import os

if not os.path.isdir("data"):
    os.mkdir("data")

app = Flask(__name__, template_folder="templates")
UPLOAD_PATH = "data/"
app.config["UPLOAD_PATH"] = UPLOAD_PATH

@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")

@app.route("/save_data/", methods=["GET", "POST"])
def save_data():
    if request.method == "GET":
        return {"response": "200"}
    
    elif request.method == "POST":
        file = request.files["image"]
        try:
            file.save(os.path.join(app.config["UPLOAD_PATH"], file.filename))
            
        except:
            pass

if __name__ == "__main__":
    app.run(debug=True)