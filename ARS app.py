import streamlit as st
import pandas as pd
import pickle

# Load the trained model or data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('Recommendation_Systems_Learner_Notebook_Full_Code.csv')  
        return data
    except FileNotFoundError:
        st.error("Dataset file not found. Please upload the dataset.")
        return None

@st.cache_data
def load_model():
    try:
        model = pickle.load(open('Recommendation_Systems_Learner_Notebook_Full_Code.pkl', 'rb'))  
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the model.")
        return None

# Main app interface
st.title("Recommendation System")

menu = ["Home", "Recommend", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Recommendation System")
    st.write("This system helps you to get recommendations based on your preferences.")

elif choice == "Recommend":
    st.subheader("Get Your Recommendation")

    data = load_data("C:\Users\hp\DOC DEVOIR MANJAKA Amazone\ratings_Electronics.csv")
    model = load_model()

    if data is not None and model is not None:
        user_input = st.selectbox("Select Item", data['Item'].unique())
        if st.button("Recommend"):
            recommendations = model.recommend(user_input)
            st.write("### Top Recommendations")
            for rec in recommendations:
                st.write(rec)

elif choice == "About":
    st.subheader("About this App")
    st.write("This is a simple Recommendation System built using Streamlit and Machine Learning.")
    st.write("Created by Gelase.")

# Footer
st.markdown("---")
st.text("Built with ❤️ by Gelase")
