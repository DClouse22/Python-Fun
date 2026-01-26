import streamlit as st
import random

st.title("🎮 Rock Paper Scissors")

# Initialize session state for score tracking
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'losses' not in st.session_state:
    st.session_state.losses = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0

# Display scoreboard
col1, col2, col3 = st.columns(3)
col1.metric("Wins", st.session_state.wins)
col2.metric("Losses", st.session_state.losses)
col3.metric("Ties", st.session_state.ties)

st.divider()

# User choice buttons
st.subheader("Make your choice:")
col1, col2, col3 = st.columns(3)

with col1:
    rock = st.button("🪨 Rock", use_container_width=True)
with col2:
    paper = st.button("📄 Paper", use_container_width=True)
with col3:
    scissors = st.button("✂️ Scissors", use_container_width=True)

# Determine user choice
user_choice = None
if rock:
    user_choice = 'rock'
elif paper:
    user_choice = 'paper'
elif scissors:
    user_choice = 'scissors'

# Game logic
if user_choice:
    computer_choice = random.choice(['scissors', 'rock', 'paper'])
    
    # Display choices
    choice_emoji = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    
    st.subheader("Results:")
    rcol1, rcol2 = st.columns(2)
    rcol1.write(f"**You chose:** {choice_emoji[user_choice]} {user_choice.title()}")
    rcol2.write(f"**Computer chose:** {choice_emoji[computer_choice]} {computer_choice.title()}")
    
    # Determine winner
    if computer_choice == user_choice:
        st.info("🤝 It's a Tie!")
        st.session_state.ties += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors' or 
          user_choice == 'paper' and computer_choice == 'rock' or 
          user_choice == 'scissors' and computer_choice == 'paper'):
        st.success("🎉 You Win!")
        st.session_state.wins += 1
    else:
        st.error("😢 You Lose!")
        st.session_state.losses += 1
    
    st.rerun()

# Reset button
if st.button("Reset Score"):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.ties = 0
    st.rerun()
