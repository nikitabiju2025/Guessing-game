import streamlit as st
import random

st.title("🎯 Simple Number Guessing Game")

# Initialize a random number only once per session
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 50)

guess = st.number_input("Guess a number between 1 and 50", min_value=1, max_value=50, step=1)

if st.button("Check"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 50)
    elif guess < st.session_state.number:
        st.info("📉 Too low! Try again.")
    else:
        st.info("📈 Too high! Try again.")
