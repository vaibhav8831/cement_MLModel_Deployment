import streamlit as st
import numpy as np
import pickle
import os

st.title('Machine Learning Streamlit Model')
st.markdown('---')

# Load pickle file
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

with open(model_path, 'rb') as file:
    model = pickle.load(file)
# Input fields for all 8 features
st.subheader('Enter Mixture Components')

cement = st.number_input('Cement (kg in a m^3 mixture)', value=540.0)
slag = st.number_input('Blast Furnace Slag (kg in a m^3 mixture)', value=0.0)
fly_ash = st.number_input('Fly Ash (kg in a m^3 mixture)', value=0.0)
water = st.number_input('Water (kg in a m^3 mixture)', value=162.0)
superplasticizer = st.number_input('Superplasticizer (kg in a m^3 mixture)', value=2.5)
coarse_agg = st.number_input('Coarse Aggregate (kg in a m^3 mixture)', value=1040.0)
fine_agg = st.number_input('Fine Aggregate (kg in a m^3 mixture)', value=676.0)
age = st.number_input('Age (day)', value=28.0)

if st.button('Predict'):
    features = np.array([[cement, slag, fly_ash, water, 
                          superplasticizer, coarse_agg, fine_agg, age]])
    prediction = model.predict(features)
    st.success(f'Predicted Compressive Strength: {prediction[0]:.2f} MPa')