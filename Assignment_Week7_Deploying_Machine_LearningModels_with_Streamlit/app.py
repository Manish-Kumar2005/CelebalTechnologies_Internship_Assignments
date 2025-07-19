import streamlit as st
import pickle
import numpy as np

with open("classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title(" Iris Flower Species Prediction")
st.write("Enter sepal and petal measurements below:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]

    species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    species = species_map.get(prediction, "Unknown")

    st.success(f" Predicted Iris Species: **{species}**")
