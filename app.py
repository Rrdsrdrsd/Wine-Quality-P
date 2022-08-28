import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))
df=pickle.load(open('Input.pkl','rb'))

st.title("Wine Quality")

fixed_acidity = st.number_input('Enter Fixed Acidity',min_value=0.00,max_value=20.00)

volatile_acidity = st.number_input('Enter Volatile Acidity',min_value=0.00,max_value=2.00)

citric_acid = st.number_input('Enter Citric Acidty',min_value=0.00,max_value=2.00)

residual_sugar = st.number_input('Enter Residual Sugar',min_value=0.00,max_value=20.00)

chlorides = st.number_input('Enter Chlorides',min_value=0.000,max_value=1.000)

free_sulfur_dioxide = st.number_input('Enter Free Sulphur-dioxide',min_value=1.00,max_value=100.00)

total_sulfur_dioxide = st.number_input('Enter Total Sulphur-dioxide',min_value=1.00,max_value=300.00)

density = st.number_input('Enter Density',min_value=0.00000,max_value=1.00000)

pH = st.number_input('Enter PH Value',min_value=0.00,max_value=14.00)

sulphates = st.number_input('Enter Sulphates',min_value=0.00,max_value=2.00)

alcohol = st.number_input('Enter Amount of Alcohol',min_value=0.00,max_value=20.00)

if st.button('Check Wine Quality'):
    query = np.array([fixed_acidity,volatile_acidity, citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol])
    query = query.reshape(1,11)
    print(query)
    
    if model.predict(query)[0]==0:
        st.title("The wine Quality is Bad ")
       
    else:
        st.title("The Wine Quality is Good ")
       