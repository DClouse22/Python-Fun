import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Math Fun for Kids",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for fun styling
st.markdown("""
    <style>
    .big-font {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
    }
    .medium-font {
        font-size: 32px;
        text-align: center;
        color: #4ECDC4;
    }
    .score-box {
        background-color: #FFE66D;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #2C3E50;
    }
    .correct-msg {
        background-color: #95E1D3;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #27AE60;
    }
    .incorrect-msg {
        background-color: #FFB6B9;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #C0392B;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'problem_answered' not in st.session_state:
    st.session_state.problem_answered = False

# Fun messages
correct_messages = [
    "🎉 Amazing! You got it!",
    "⭐ Fantastic work!",
    "🌟 You're a math superstar!",
    "🚀 Excellent job!",
    "💪 You're so smart!",
    "🎊 Awesome answer!",
]

incorrect_messages = [
    "😊 Not quite! Try again!",
    "💭 That's not it. Give it another try!",
    "🤔 Close! Try the next one!",
]

# Title
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="big-font">🎓 Math Fun! 🎓</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="score-box">Score: {st.session_state.score}/{st.session_state.attempts}</div>', unsafe_allow_html=True)

st.write("---")

# Tabs for different activities
tab1, tab2, tab3, tab4 = st.tabs(["➕ Addition", "➖ Subtraction", "📊 Progress", "🎮 Games"])

with tab1:
    st.markdown('<div class="medium-font">Addition Practice</div>', unsafe_allow_html=True)
    
    difficulty = st.radio("Choose difficulty:", ["Easy (0-5)", "Medium (0-10)", "Hard (0-20)"], horizontal=True, key="add_difficulty")
    
    if difficulty == "Easy (0-5)":
        max_num = 5
    elif difficulty == "Medium (0-10)":
        max_num = 10
    else:
        max_num = 20
    
    # Generate problem
    if st.button("Get a new problem! ➕", key="new_add"):
        num1 = random.randint(0, max_num)
        num2 = random.randint(0, max_num)
        st.session_state.current_problem = {
            'num1': num1,
            'num2': num2,
            'type': 'addition'
        }
        st.session_state.problem_answered = False
    
    if st.session_state.current_problem and st.session_state.current_problem['type'] == 'addition':
        num1 = st.session_state.current_problem['num1']
        num2 = st.session_state.current_problem['num2']
        
        # Display problem with visual aids
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="big-font">{num1}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="big-font">+</div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="big-font">{num2}</div>', unsafe_allow_html=True)
        
        # Visual representation with emojis
        st.write("🌟 " * num1)
        st.write("⭐ " * num2)
        
        # Answer input
        answer = st.number_input("What's the answer?", min_value=0, max_value=100, step=1, key="add_answer")
        
        if st.button("Check Answer! ✓", key="check_add") and not st.session_state.problem_answered:
            correct_answer = num1 + num2
            st.session_state.attempts += 1
            
            if answer == correct_answer:
                st.session_state.score += 1
                st.markdown(f'<div class="correct-msg">{random.choice(correct_messages)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="correct-msg">✓ {num1} + {num2} = {correct_answer}</div>', unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f'<div class="incorrect-msg">{random.choice(incorrect_messages)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="incorrect-msg">The correct answer is {correct_answer}</div>', unsafe_allow_html=True)
            
            st.session_state.history.append({
                'problem': f'{num1} + {num2}',
                'your_answer': answer,
                'correct_answer': correct_answer,
                'correct': answer == correct_answer
            })
            st.session_state.problem_answered = True

with tab2:
    st.markdown('<div class="medium-font">Subtraction Practice</div>', unsafe_allow_html=True)
    
    difficulty = st.radio("Choose difficulty:", ["Easy (0-5)", "Medium (0-10)", "Hard (0-20)"], horizontal=True, key="sub_difficulty")
    
    if difficulty == "Easy (0-5)":
        max_num = 5
    elif difficulty == "Medium (0-10)":
        max_num = 10
    else:
        max_num = 20
    
    # Generate problem
    if st.button("Get a new problem! ➖", key="new_sub"):
        num1 = random.randint(0, max_num)
        num2 = random.randint(0, num1)  # Ensure num2 <= num1 to avoid negative answers
        st.session_state.current_problem = {
            'num1': num1,
            'num2': num2,
            'type': 'subtraction'
        }
        st.session_state.problem_answered = False
    
    if st.session_state.current_problem and st.session_state.current_problem['type'] == 'subtraction':
        num1 = st.session_state.current_problem['num1']
        num2 = st.session_state.current_problem['num2']
        
        # Display problem with visual aids
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="big-font">{num1}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="big-font">−</div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="big-font">{num2}</div>', unsafe_allow_html=True)
        
        # Visual representation with emojis
        st.write("🎈 " * num1)
        st.write("❌ " * num2)
        
        # Answer input
        answer = st.number_input("What's the answer?", min_value=0, max_value=100, step=1, key="sub_answer")
        
        if st.button("Check Answer! ✓", key="check_sub") and not st.session_state.problem_answered:
            correct_answer = num1 - num2
            st.session_state.attempts += 1
            
            if answer == correct_answer:
                st.session_state.score += 1
                st.markdown(f'<div class="correct-msg">{random.choice(correct_messages)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="correct-msg">✓ {num1} − {num2} = {correct_answer}</div>', unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f'<div class="incorrect-msg">{random.choice(incorrect_messages)}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="incorrect-msg">The correct answer is {correct_answer}</div>', unsafe_allow_html=True)
            
            st.session_state.history.append({
                'problem': f'{num1} − {num2}',
                'your_answer': answer,
                'correct_answer': correct_answer,
                'correct': answer == correct_answer
            })
            st.session_state.problem_answered = True

with tab3:
    st.markdown('<div class="medium-font">📊 Your Progress</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Score", f"{st.session_state.score}/{st.session_state.attempts}")
    
    with col2:
        if st.session_state.attempts > 0:
            percentage = (st.session_state.score / st.session_state.attempts) * 100
            st.metric("Success Rate", f"{percentage:.0f}%")
        else:
            st.metric("Success Rate", "N/A")
    
    with col3:
        st.metric("Problems Solved", st.session_state.attempts)
    
    if st.session_state.history:
        st.write("### Recent Problems:")
        df = pd.DataFrame(st.session_state.history[-10:])
        df['Status'] = df['correct'].apply(lambda x: "✓ Correct" if x else "✗ Incorrect")
        st.dataframe(
            df[['problem', 'your_answer', 'correct_answer', 'Status']],
            use_container_width=True,
            hide_index=True,
            column_config={
                'problem': 'Problem',
                'your_answer': 'Your Answer',
                'correct_answer': 'Correct Answer',
                'Status': 'Status'
            }
        )
        
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.session_state.score = 0
            st.session_state.attempts = 0
            st.rerun()

with tab4:
    st.markdown('<div class="medium-font">🎮 Fun Games</div>', unsafe_allow_html=True)
    
    game_choice = st.radio("Pick a game:", ["Number Matching", "Number Sequence"], horizontal=True)
    
    if game_choice == "Number Matching":
        st.write("Find the pair! Which numbers add up?")
        
        # Create pairs that add up
        target = st.slider("Target sum:", 5, 20, 10)
        
        if st.button("Generate new pairs! 🎲"):
            pairs = []
            for _ in range(4):
                a = random.randint(1, target-1)
                b = target - a
                pairs.append((a, b))
            st.session_state.pairs = pairs
        
        if 'pairs' in st.session_state:
            cols = st.columns(2)
            for idx, (a, b) in enumerate(st.session_state.pairs):
                with cols[idx % 2]:
                    if st.button(f"🔹 {a} + {b} = ?", key=f"pair_{idx}"):
                        result = a + b
                        st.success(f"🎉 {a} + {b} = {result}!")
    
    else:  # Number Sequence
        st.write("Complete the sequence!")
        
        sequence_type = st.radio("Type:", ["Counting up", "Counting down"], horizontal=True)
        
        if st.button("Get new sequence! 🎲"):
            start = random.randint(1, 15)
            if sequence_type == "Counting up":
                st.session_state.sequence = list(range(start, start + 5))
            else:
                st.session_state.sequence = list(range(start, start - 5, -1))
        
        if 'sequence' in st.session_state:
            seq = st.session_state.sequence
            # Hide one number
            hide_idx = random.randint(0, len(seq) - 1)
            display_seq = [f"**{x}**" if i != hide_idx else "**?**" for i, x in enumerate(seq)]
            
            st.write("   ".join(display_seq))
            
            answer = st.number_input("What number is the ?", min_value=0, max_value=100, step=1, key="sequence_answer")
            
            if st.button("Check! ✓"):
                if answer == seq[hide_idx]:
                    st.success(f"🎉 Correct! It's {seq[hide_idx]}!")
                else:
                    st.error(f"Not quite! The answer is {seq[hide_idx]}")

# Footer
st.write("---")
st.write("🌟 Keep practicing and you'll be a math expert! 🌟")
