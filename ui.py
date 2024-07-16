# Import necessary libraries
import streamlit as st
from predictor import predict_score

# Set the title of the Streamlit app
st.title("Football Score Predictor")

# Description of the app
st.write("""
This app predicts the score of a football match between two teams. Enter the names of the teams and click the "Predict Score" button to get the predicted scores.
""")

# Create input boxes for the team names
team1 = st.text_input("Enter the name of Team 1:", "")
team2 = st.text_input("Enter the name of Team 2:", "")

# Create a button to predict the score
if st.button("Predict Score"):
    # Check if the user has entered names for both teams
    if team1 and team2:
        # Predict the scores using the predict_score function
        score1, score2 = predict_score(team1, team2)
        
        # Display the predicted scores
        st.write(f"### Predicted Score:")
        st.write(f"{team1}: {score1}")
        st.write(f"{team2}: {score2}")
    else:
        # Display a message if team names are missing
        st.write("Please enter names for both teams to predict the score.")
