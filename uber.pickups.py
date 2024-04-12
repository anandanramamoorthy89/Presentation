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

