# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:14:50 2024

@author: Coenraad Reichel
"""

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np


# Load the trained model
# Code For when not deployed model = pickle.load(open('C:/Users/Coenraad Reichel/OneDrive - Eduvos/Documents/Eduvos Honours/ITDAA4-12/Project/Final Code/Trained_model.sav', 'rb'))

model = pickle.load(open('https://github.com/CoenraadReichel1234/itdaa-health-prediction/blob/main/Trained_model.sav', 'rb'))

def heart_predict(patient_data):
    
    
    

    np_input = np.asarray(patient_data)
    np_reshaped = np_input.reshape(1,-1)

    prediction = model.predict(np_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Patient Heart is Healthy'
    else:
        return 'Heart is Unhealthy'
    
def main():
    
    st.set_page_config(page_title="Heart Checks", page_icon=":cold_sweat:", layout="wide")
    st.title("Heart Prediction System")



    # Options
    sex_options = {"Male": 1, "Female": 0}
    cp_options = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Typical Angina": 2, "Asymptomatic": 3}
    fbs_options = {"True": 1, "False":0}
    restecg_options = {"Normal": 0, "Abnormal": 1, "Ventricular hypertrophy": 2}
    exang_options = {"Yes": 1, "No": 0}
    slope_options = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    thal_options = {"Unkown": 0, "Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
    
    # Collect patient data
    age = st.number_input("Age", min_value=0, max_value=120)
    
    sexView = st.selectbox("Select your Gender:", list(sex_options.keys()))
    sex = sex_options[sexView]
    
    cpView = st.selectbox("Chest Pain:", list(cp_options.keys()))
    cp = cp_options[cpView]
    
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    
    chol = st.number_input("Serum Cholestoral in mg/dl", min_value=0)
    
    fbsView = st.selectbox("Fasting Blood Sugar >120mg/dl:", list(fbs_options.keys()))
    fbs = fbs_options[fbsView]
    
    restecgView = st.selectbox("Resting Electrocardiographic:", list(restecg_options.keys()))
    restecg = restecg_options[restecgView]
    
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
    
    exangView = st.selectbox("Exercise Induced Angina:", list(exang_options.keys()))
    exang = exang_options[exangView]
    
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, format="%.2f")
    
    slopeView = st.selectbox("Slope of peak exercise ST segment:", list(slope_options.keys()))
    slope = slope_options[slopeView]
    
    ca = st.number_input("Number of major vessels colored by fluoroscopy", min_value=0)
    
    thalView = st.selectbox("Status of your heart:", list(thal_options.keys()))
    thal = thal_options[thalView]
    


    diagnosis = ''
    
    #button
    if st.button("Diagnose Heart Health"):
        diagnosis = heart_predict([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()
