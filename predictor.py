# predictor.py

import random

def predict_score(team1, team2):
    # This is a simple random predictor. Replace with your actual prediction logic.
    score1 = random.randint(0, 5)
    score2 = random.randint(0, 5)
    return score1, score2
