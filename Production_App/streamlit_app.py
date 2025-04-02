import torch
import streamlit as st

# Load the scripted model and set to evaluation mode.
model = torch.jit.load('/Users/arponbiswas/Deep-Learning-Prejects/NeuroCalculator/Models/scripted_model.pt', map_location='cpu')
model.eval()

# Custom CSS styling.
st.markdown(
    """
    <style>
    .main {
        background-color: black;
    }
    .title {
        font-size: 3rem;
        text-align: center;
        color: #4CAF50;
    }
    .input-container {
        text-align: center;
        margin-top: 20px;
    }
    .result {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 30px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description.
st.markdown('<p class="title">Neural Calculator</p>', unsafe_allow_html=True)
st.markdown("### Enter two numbers:")

# Input fields for numbers.
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Number 1", value=100.0)
with col2:
    num2 = st.number_input("Number 2", value=100.0)

# Button to trigger prediction.
if st.button("Calculate Sum"):
    sample = torch.tensor([[num1, num2]])
    with torch.no_grad():
        prediction = model(sample)
    st.markdown(f'<p class="result">Predicted Sum: {prediction.item()}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="result">Actual Sum: {num1+num2}</p>', unsafe_allow_html=True)