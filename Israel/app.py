import pickle
from flask import Flask, request, render_template


app = Flask(__name__)

model_files = {
    "US": "USnukepredictmodel.sav",
    "RU": "RUnukepredictmodel.sav",
    "CN": "CNnukepredictmodel.sav",
    "FR": "FRnukepredictmodel.sav",
    "UK": "UKnukepredictmodel.sav"
}

loaded_models = {country: pickle.load(open(f"/workspaces/Israel-Flask-Project/Israel/{filename}", 'rb'))
                 for country, filename in model_files.items()}

@app.route("/", methods = ["GET", "POST"])

def index():
    selected_model = None

    if request.method == "POST":
        country_select = request.form["country"]  # Get selected country code from form
        selected_model = loaded_models.get(country_select)  # Retrieve the corresponding model

    return render_template('index.html', selected_model=selected_model)
