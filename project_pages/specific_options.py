import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os.path
from project_pages.utils import runAndSave


def specific_options(savedModel):
    st.title("Enter Patient Information")

    fields = [
        'FILE NO', 'Age', 'Gender', 'Place of Habitation', 'Annual Income', 
        'Smoking Status', 'Alcohol', 'Tobacco Chewing Status', 'Comorbidities', 
        'ECOG PS', 'BMI', 'Bipedal Edema', 'Site of Primary Cancer', 'Stage', 
        'Chemotherapy Protocol', 'Cycle Number', 'Dosing of Chemotherapy', 
        'Use of Prophylactic Growth Factors', 'Haemoglobin', 'WBC', 
        'Absolute Lymphocytes', 'Absolute Neutrophil Count', 
        'Neutrophil to Lymphocyte ratio', 'Total Platelet count', 
        'Serum Albumin', 'Serum Creatinine', 'Eosinophils', 'Basophils', 'Monocytes'
    ]

    few_fields = [
        'Age', 'Gender', 'Place of Habitation', 'Annual Income', 
        'Smoking Status', 'Alcohol', 'Tobacco Chewing Status', 'Comorbidities', 
        'ECOG PS', 'BMI', 'Bipedal Edema', 'Site of Primary Cancer', 'Stage', 
        'Chemotherapy Protocol', 'Cycle Number', 'Dosing of Chemotherapy', 
        'Use of Prophylactic Growth Factors', 'Haemoglobin', 'WBC', 
        'Absolute Lymphocytes', 'Absolute Neutrophil Count', 
        'Neutrophil to Lymphocyte ratio', 'Total Platelet count', 
        'Serum Albumin', 'Serum Creatinine', 'Eosinophils', 'Basophils', 'Monocytes'
    ]

    input_data_dict = {field: -1 for field in fields}
    input_data = pd.DataFrame([input_data_dict])


    # input_data = {}
    input_data["FILE NO"] = st.text_input("FILE NO", value="", help="Enter the patient's file number.")
    
    if not input_data["FILE NO"].values[0]:
        st.error("FILE NO is a compulsory field.")
        return

    # Field selection checkboxes
    st.sidebar.header("Select Fields to Enter")
    selected_fields = {
        "Stage": st.sidebar.checkbox("Stage"),
        "Serum Albumin": st.sidebar.checkbox("Serum Albumin"),
        "Chemotherapy Protocol": st.sidebar.checkbox("Chemotherapy Protocol"),
        "Serum Creatinine": st.sidebar.checkbox("Serum Creatinine"),
        "BMI": st.sidebar.checkbox("BMI"),
        "WBC": st.sidebar.checkbox("WBC"),
        "Neutrophil to Lymphocyte ratio": st.sidebar.checkbox("Neutrophil to Lymphocyte ratio"),
        "Absolute Neutrophil Count": st.sidebar.checkbox("Absolute Neutrophil Count"),
        "Use of Prophylactic Growth Factors": st.sidebar.checkbox("Use of Prophylactic Growth Factors"),
        "Age": st.sidebar.checkbox("Age"),
        "Cycle Number": st.sidebar.checkbox("Cycle Number"),
        "Total Platelet count": st.sidebar.checkbox("Total Platelet count"),
        "Gender": st.sidebar.checkbox("Gender"),
        "ECOG PS": st.sidebar.checkbox("ECOG PS"),
        "Eosinophils": st.sidebar.checkbox("Eosinophils"),
        "Dosing of Chemotherapy": st.sidebar.checkbox("Dosing of Chemotherapy"),
        "Place of Habitation": st.sidebar.checkbox("Place of Habitation"),
        "Absolute Lymphocytes": st.sidebar.checkbox("Absolute Lymphocytes"),
        "Annual Income": st.sidebar.checkbox("Annual Income"),
        "Comorbidities": st.sidebar.checkbox("Comorbidities"),
        "Basophils": st.sidebar.checkbox("Basophils"),
        "Monocytes": st.sidebar.checkbox("Monocytes"),
        "Smoking Status": st.sidebar.checkbox("Smoking Status"),
        "Haemoglobin": st.sidebar.checkbox("Haemoglobin"),
        "Bipedal Edema": st.sidebar.checkbox("Bipedal Edema"),
        "Tobacco Chewing Status": st.sidebar.checkbox("Tobacco Chewing Status"),
        "Site of Primary Cancer": st.sidebar.checkbox("Site of Primary Cancer"),
        "Alcohol": st.sidebar.checkbox("Alcohol")
    }

    
    selected_field_names = [field for field, selected in selected_fields.items() if selected]
    num_columns = 3
    columns = st.columns(num_columns)
    for idx, field in enumerate(selected_field_names):
        with columns[idx % num_columns]:
            if field == "Age":
                input_data["Age"] = st.text_input("Age")
            elif field == "Gender":
                input_data["Gender"] = st.selectbox("Gender", ["Male", "Female"])
            elif field == "Place of Habitation":
                input_data["Place of Habitation"] = st.selectbox("Place of Habitation", ["Urban", "Rural"])
            elif field == "Annual Income":
                input_data["Annual Income"] = st.selectbox("Annual Income", ["BPL", "Non-BPL"])
            elif field == "Smoking Status":
                input_data["Smoking Status"] = st.selectbox("Smoking Status", ["Smoker", "Non-smoker"])
            elif field == "Alcohol":
                input_data["Alcohol"] = st.selectbox("Alcohol", ["Alcoholic", "Non-alcoholic"])
            elif field == "Tobacco Chewing Status":
                input_data["Tobacco Chewing Status"] = st.selectbox("Tobacco Chewing Status", ["Yes", "No"])
            elif field == "Comorbidities":
                input_data["Comorbidities"] = st.selectbox("Comorbidities", ["Yes", "No"])
            elif field == "ECOG PS":
                input_data["ECOG PS"] = st.text_input("ECOG PS")
            elif field == "BMI":
                input_data["BMI"] = st.selectbox("BMI", ["Normal", "Underweight", "Overweight/Obese"])
            elif field == "Bipedal Edema":
                input_data["Bipedal Edema"] = st.selectbox("Bipedal Edema", ["Yes", "No"])
            elif field == "Site of Primary Cancer":
                input_data["Site of Primary Cancer"] = st.selectbox("Site of Primary Cancer", ["HAEMATOLOGICAL", "NON HAEMATOLOGICAL"])
            elif field == "Stage":
                input_data["Stage"] = st.selectbox("Stage", ["Early (Stage 1 &2)", "Stage 3", "Stage 4"])
            elif field == "Chemotherapy Protocol":
                input_data["Chemotherapy Protocol"] = st.selectbox("Chemotherapy Protocol", ["Single agent", "Doublet", "Triplet"])
            elif field == "Cycle Number":
                input_data["Cycle Number"] = st.text_input("Cycle Number")
            elif field == "Dosing of Chemotherapy":
                input_data["Dosing of Chemotherapy"] = st.selectbox("Dosing of Chemotherapy", ["Standard", "Compromised"])
            elif field == "Use of Prophylactic Growth Factors":
                input_data["Use of Prophylactic Growth Factors"] = st.selectbox("Use of Prophylactic Growth Factors", ["Yes", "No"])
            elif field == "Haemoglobin":
                input_data["Haemoglobin"] = st.text_input("Haemoglobin")
            elif field == "WBC":
                input_data["WBC"] = st.text_input("WBC")
            elif field == "Absolute Lymphocytes":
                input_data["Absolute Lymphocytes"] = st.text_input("Absolute Lymphocytes")
            elif field == "Absolute Neutrophil Count":
                input_data["Absolute Neutrophil Count"] = st.text_input("Absolute Neutrophil Count")
            elif field == "Neutrophil to Lymphocyte ratio":
                input_data["Neutrophil to Lymphocyte ratio"] = st.text_input("Neutrophil to Lymphocyte ratio")
            elif field == "Total Platelet count":
                input_data["Total Platelet count"] = st.text_input("Total Platelet count")
            elif field == "Serum Albumin":
                input_data["Serum Albumin"] = st.text_input("Serum Albumin")
            elif field == "Serum Creatinine":
                input_data["Serum Creatinine"] = st.text_input("Serum Creatinine")
            elif field == "Eosinophils":
                input_data["Eosinophils"] = st.text_input("Eosinophils")
            elif field == "Basophils":
                input_data["Basophils"] = st.text_input("Basophils")
            elif field == "Monocytes":
                input_data["Monocytes"] = st.text_input("Monocytes")
    
   
    input = input_data.copy()
    input_df = input[few_fields]

    # Prediction button
    col_left, col_right = st.columns([3, 1])

    button_style = """
        <style>
        .stButton > button {
            width: 300px;
            height: 40px;
            padding: 10px 20px;
            font-size: 20px;
            border-radius: 10px;
            color: white;
            border: 2px solid #FFFFFF;
            cursor: pointer;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    with col_right:

        if st.button("Predict hematological toxicity"): 
            data_append = runAndSave(input_df,input_data,savedModel)
    return data_append


if __name__ == "__main__":
    specific_options()
