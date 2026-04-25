import pickle
from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Import ridge regressor and standard scaler pickled files
ridge_model = pickle.load(open('ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Extract features from form — adjust field names to match your HTML form
            features = [float(request.form.get(field)) for field in [
                'Temperature',
                'RH',
                'Ws',
                'Rain',
                'FFMC',
                'DMC',
                'ISI',
                'Classes',
                'Region'# adjust or remove if not an input feature
            ]]

            # Scale and predict
            data = standard_scaler.transform([features])
            result = ridge_model.predict(data)[0]

            return render_template('home.html', result=round(result, 2))

        except Exception as e:
            return render_template('home.html', result=f"Error: {str(e)}")

    # GET request
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")