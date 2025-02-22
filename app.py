import streamlit as st
import random

# Title & Introduction
st.title("Growth Mindset Challenge")
st.write("A growth mindset is the belief that intelligence and abilities can be developed with effort and learning.")

# List of motivational quotes
quotes = [
    "Failure is simply the opportunity to begin again, this time more intelligently. – Henry Ford",
    "Do not be embarrassed by your failures, learn from them and start again. – Richard Branson",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Believe you can and you’re halfway there. – Theodore Roosevelt"
]

# Select a random quote each time the app runs
random_quote = random.choice(quotes)

# Display the quote
st.subheader("Motivational Quote of the Day:")
st.write(random_quote)

# User Input Section
user_input = st.text_input("What is your biggest challenge right now?")
if user_input:
    st.write(f"That's a great challenge to tackle! Stay focused and keep a growth mindset. 💪")

# Interactive Elements
if st.button("Get Another Quote"):
    random_quote = random.choice(quotes)  # Pick another quote when the button is clicked
    st.write(random_quote)
