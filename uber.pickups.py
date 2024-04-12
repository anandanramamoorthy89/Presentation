import streamlit as st
import pandas as pd
import numpy as np

st.title('Survey - ML and Data science')
st.sidebar.title("Contents")
pages = ["Exploration","DataViz","Modelling"]
pages=st.sidebar.radio("Go to", pages)

import pandas as pd
import numpy as np
#read csv and only mark empty cells as NaN so that "None" doesn't vanish
df=pd.read_csv(r"C:\Users\anand\Downloads\kaggle-survey-2020\kaggle_survey_2020_responses.csv",na_values=[''],keep_default_na=False)

question = df.loc[0]
df=df.drop(0)
print(df.columns)

import streamlit as st
import pandas as pd

# Define Streamlit app layout
st.title('Kaggle Survey Data Viewer')
st.write('Upload a Kaggle survey data CSV file to view its contents.')

# Add file uploader widget
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Read CSV and mark empty cells as NaN
    df = pd.read_csv(uploaded_file, na_values=[''], keep_default_na=False)
    
    # Display data
    st.write('## Survey Data')
    st.write(df.head())  # Display first few rows of the dataframe
    st.write(f"Total rows: {len(df)}, Total columns: {len(df.columns)}")
