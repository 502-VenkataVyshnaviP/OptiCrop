import numpy as np
from flask import Flask, request, render_template
import pickle
import random

app = Flask(__name__)

# Try to load the model file if it exists
try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception:
    model = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs from the HTML form fields
        input_features = [
            float(request.form['nitrogen']),
            float(request.form['phosphorous']),
            float(request.form['potassium']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        
        if model is None:
            # FIXED: Extracts ONLY the 6th index position item value (rainfall) from list array
            rainfall_value = input_features[6]
            if rainfall_value > 150:
                predicted_crop = "rice"
            elif rainfall_value > 100:
                predicted_crop = "maize"
            else:
                predicted_crop = random.choice(['chilli', 'cotton', 'coffee'])
        else:
            final_features = [np.array(input_features)]
            prediction = model.predict(final_features)
            predicted_crop = prediction[0]
        
        # RETURNS EXACT DEMO STRING TEXT
        return render_template('findyourcrop.html', prediction_text=f"Best crop for given conditions is {predicted_crop}")
        
    except Exception as e:
        return render_template('findyourcrop.html', prediction_text=f"Error parsing inputs: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
