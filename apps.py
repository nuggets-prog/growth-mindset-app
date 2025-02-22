import streamlit as st
import random

# App Title
st.title("Growth Mindset Challenge")

# Introduction Section
st.write("""
A growth mindset is the belief that intelligence and abilities can be developed with effort and learning. 
This concept, popularized by psychologist Carol Dweck, teaches us that every challenge is an opportunity to improve.
""")

# Motivational Quotes List
quotes = [
    "Failure is simply the opportunity to begin again, this time more intelligently. – Henry Ford",
    "Do not be embarrassed by your failures, learn from them and start again. – Richard Branson",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. – Jim Rohn"
]

# Display Random Motivational Quote
random_quote = random.choice(quotes)
st.subheader("💡 Motivational Quote:")
st.write(f"_{random_quote}_")

# User Input Section
st.subheader("📌 Share Your Thoughts")
user_input = st.text_input("What is your biggest challenge right now?")
if user_input:
    st.write(f"That's a great challenge to tackle! Stay focused and keep a growth mindset. 💪")

# Growth Mindset Tips
st.subheader("🚀 Why Adopt a Growth Mindset?")
st.write("""
- **Embrace Challenges**: View obstacles as opportunities to learn rather than as setbacks.  
- **Learn from Mistakes**: Making mistakes is a natural part of learning. Each error is a chance to improve.  
- **Persist Through Difficulties**: Stay determined, even when things get tough. Hard work and persistence lead to growth.  
- **Celebrate Effort**: Recognize and reward effort, not just results.  
- **Keep an Open Mind**: Stay curious and be willing to adapt your approach based on what you learn.  
""")

# Interactive Elements
st.subheader("🎯 Interactive Elements")
progress = st.slider("How strongly do you believe in a growth mindset?", 0, 100, 50)
st.progress(progress / 100)

if st.button("Get Inspired!"):
    st.write(f"🚀 **Remember:** {random.choice(quotes)}")

# Footer Message
st.write("🌟 *Your journey in education isn’t just about proving your intelligence—it’s about developing it!* 🌟")
st.write("🌟 *Learning isn’t about being the smartest—it’s about becoming better every day!* 🌟")
st.write("🌟 *Education isn’t just about showing what you know—it’s about growing into what you can become!* 🌟")

st.write(f"🚀 **Remember:** {random.choice(quotes)}")