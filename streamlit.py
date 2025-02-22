import streamlit as st
import random

# Title
st.title("🚀 Growth Mindset Challenge!")

# Introduction
st.write("""
A **growth mindset** means believing that you can develop abilities through 
hard work and learning. Are you ready to challenge yourself and grow? 🌱
""")

# User Input
user_goal = st.text_input("What’s one goal you’re working on?")

# Motivational Messages
quotes = [
    "Mistakes are proof that you're trying!",
    "Believe you can, and you're halfway there.",
    "Every expert was once a beginner.",
    "Keep going. Every challenge makes you stronger!"
]

if st.button("Get a Motivational Quote"):
    st.write(random.choice(quotes))

# Progress Bar Example
progress = st.slider("How confident do you feel about your progress?", 0, 100, 50)
st.progress(progress / 100)

st.success("Keep pushing forward! You're on the right path. 💪")
