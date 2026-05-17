import pandas as pd
from sklearn.linear_model import LinearRegression


# Load Dataset

data = pd.read_csv("Housing.csv")   # make sure file is in same folder
data = data.dropna()


# Features & Target

X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = data['price']


# Train Model

model = LinearRegression()
model.fit(X, y)


# CLI Loop

print("=== House Price Prediction CLI ===")

while True:
    try:
        print("\nEnter house details:")

        area = float(input("Area: "))
        bedrooms = float(input("Bedrooms: "))
        bathrooms = float(input("Bathrooms: "))
        stories = float(input("Stories: "))
        parking = float(input("Parking: "))

        prediction = model.predict([[area, bedrooms, bathrooms, stories, parking]])

        print(f"\nPredicted Price: {prediction[0]:.2f}")

    except Exception as e:
        print("Error:", e)

    choice = input("\nDo you want to predict again? (y/n): ")
    if choice.lower() != 'y':
        print("Exiting CLI App...")
        break