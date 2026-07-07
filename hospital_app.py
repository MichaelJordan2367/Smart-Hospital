import streamlit as st
import pandas as pd
import pickle

with oper("hospital_model.pkl") as f:
  bundle = pickle.load(f)
  st.write("conected") 
