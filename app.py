import streamlit as st
import utils
import tempfile
import os

# Define the folder where the uploaded PDF will be saved
#save_dir = './uploads/'

# Create the directory if it doesn't exist
#os.makedirs(save_dir, exist_ok=True)


pg = st.navigation(["page1.py", "page2.py", "page3.py"])
pg.run()

