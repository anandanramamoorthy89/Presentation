import streamlit as st
import pandas as pd
import numpy as np

st.title('Survey - ML and Data science')
st.sidebar.title("Contents")
pages = ["Exploration","DataViz","Modelling"]
pages=st.sidebar.radio("Go to", pages)



