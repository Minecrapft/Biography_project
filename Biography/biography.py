import streamlit as st
import datetime

# ---- Page Configuration ----
st.set_page_config(page_title="BIODATA", page_icon="📋", layout="wide")

# ---- HEADER SECTION ----
st.title("Biodata")  # large font size



# ---- Personal Information ----
st.subheader("Personal Information")  # medium font size

# Name Input
name = st.text_input("Name", "Enter your name")

# Age Selection
age = st.selectbox("Age", [str(i) for i in range(18, 101)])  # ages 18-100

# Gender Selection
gender = st.radio("Gender", ["Male", "Female"])

# ---- Family Background ----
st.subheader("Family Background")

# Mother's Name
mother = st.text_input("Mother's Name", "Enter mother's name")
mbday = st.date_input("Mother's Birthday", datetime.date(1970, 1, 1))  # Default date

# Father's Name
father = st.text_input("Father's Name", "Enter father's name")

# Guardian's Name
guardian = st.text_input("Guardian's Name", "Enter guardian's name")

# ---- Educational Attainment ----
st.subheader("Educational Attainment")

hs = st.text_input("High School", "Surigao City National Highschool")
shs = st.text_input("Senior High School", "Surigao del Norte National highschool")
college = st.text_input("College", "Surigao del Norte State University")
st.write("---")
# ---- Social Media Section ----
st.subheader("Social Media Accounts")   


st.write("[Facebook](https://facebook.com)")  # Hyperlink example

from PIL import Image


# Load the image
image = Image.open(r'C:\Users\admin\OneDrive\Documents\HAHAHA\WIN_20241109_20_19_43_Pro.jpg')

# Resize the image
resized_image = image.resize((300, 300))  # Width, Height in pixels

# Display the resized image
st.image(resized_image, caption="Resized Image (300x300)", use_column_width=False)

import streamlit as st

# Image URL or local path
image_url = "path/to/your/image.jpg"

# Custom HTML and CSS for rounded corners
custom_html = f"""
<style>
    .rounded-image {{
        border-radius: 1px; 
        width: 100%; 
        max-width: 600px; 
        margin: 0 auto; 
        display: block;
    }}
</style>
<img class="rounded-image" src="{r'C:\Users\admin\OneDrive\Documents\HAHAHA\WIN_20241109_20_19_43_Pro.jpg'}" alt="Rounded Image">
"""

# Embed the custom HTML in Streamlit
st.markdown(custom_html, unsafe_allow_html=True)
