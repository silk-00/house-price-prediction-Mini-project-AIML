from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import threading 

app = Flask(__name__)

# Load dataset
data = pd.read_csv("Housing.csv")
data = data.dropna()

# Features and target
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    stories = float(request.form['stories'])
    parking = float(request.form['parking'])

    prediction = model.predict([[area, bedrooms, bathrooms, stories, parking]])

    return render_template('index.html', prediction_text=f"Predicted Price: {prediction[0]:.2f}")


if __name__ == "__main__":
    app.run(debug=True)



    