from flask import Flask, request, render_template, send_from_directory
import pickle
import os

app = Flask(__name__)

model_files = {
    "US": "USnukepredictmodel.sav",
    "RU": "RUnukepredictmodel.sav",
    "CN": "CNnukepredictmodel.sav",
    "FR": "FRnukepredictmodel.sav",
    "UK": "UKnukepredictmodel.sav"
}

loaded_models = {country: pickle.load(open(f"/Israel/models/{filename}", 'rb'))
                 for country, filename in model_files.items()}

@app.route("/", methods=["GET", "POST"])
def index():
    country_select = None  # Default value if the form is not submitted

    if request.method == "POST":
        country_select = request.form["country"]

    return render_template('index.html', selected_model=country_select)

@app.route('/Israel/images/<country_code>output.png')
def get_image(country_code):
    image_path = os.path.join(app.root_path, 'images', f'{country_code}output.png')
    return send_from_directory(os.path.dirname(image_path), os.path.basename(image_path))


if __name__ == "__main__":
    app.run(debug=False)