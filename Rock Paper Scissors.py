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

# User choice buttons with large icons
st.subheader("Make your choice:")

# Custom CSS for larger icon display
st.markdown("""
<style>
.game-icon {
    font-size: 80px;
    text-align: center;
    padding: 10px;
    cursor: pointer;
}
.choice-label {
    text-align: center;
    font-weight: bold;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="game-icon">🪨</div>', unsafe_allow_html=True)
    st.markdown('<p class="choice-label">Rock</p>', unsafe_allow_html=True)
    rock = st.button("Select Rock", use_container_width=True, key="rock_btn")
with col2:
    st.markdown('<div class="game-icon">📄</div>', unsafe_allow_html=True)
    st.markdown('<p class="choice-label">Paper</p>', unsafe_allow_html=True)
    paper = st.button("Select Paper", use_container_width=True, key="paper_btn")
with col3:
    st.markdown('<div class="game-icon">✂️</div>', unsafe_allow_html=True)
    st.markdown('<p class="choice-label">Scissors</p>', unsafe_allow_html=True)
    scissors = st.button("Select Scissors", use_container_width=True, key="scissors_btn")

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
    
    # Display choices with large icons
    choice_emoji = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

    st.subheader("Results:")
    rcol1, rcol2 = st.columns(2)
    with rcol1:
        st.markdown(f'<div class="game-icon">{choice_emoji[user_choice]}</div>', unsafe_allow_html=True)
        st.markdown(f'<p class="choice-label">You chose: {user_choice.title()}</p>', unsafe_allow_html=True)
    with rcol2:
        st.markdown(f'<div class="game-icon">{choice_emoji[computer_choice]}</div>', unsafe_allow_html=True)
        st.markdown(f'<p class="choice-label">Computer chose: {computer_choice.title()}</p>', unsafe_allow_html=True)
    
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
