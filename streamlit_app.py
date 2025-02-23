import streamlit as st
import openai

# Set page configuration
st.set_page_config(page_title="Ibolya AI - 10-Year Future Predictor", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        body { background-color: #F5F5F5; }
        .title { font-size: 36px; font-weight: bold; color: #4A90E2; text-align: center; }
        .subtitle { font-size: 20px; text-align: center; color: #555; margin-bottom: 20px; }
        .stButton>button { background-color: #4A90E2; color: white; border-radius: 10px; font-size: 18px; padding: 10px 24px; }
        .stTextInput>div>div>input { font-size: 16px; padding: 10px; }
        .stSelectbox>div>div>select { font-size: 16px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True
)

# Function to call GPT-4 for future predictions
def get_future_scenarios(user_data):
    prompt = f"""
    You are an advanced foresight AI named Ibolya.
    Predict the user's life in 10 years based on:
    - Career: {user_data['career']}
    - Investments: {user_data['investments']}
    - Risk Tolerance: {user_data['risk_tolerance']}
    
    Provide:
    1️⃣ Best Case (If they make optimal choices)
    2️⃣ Worst Case (If they make poor choices)
    3️⃣ Most Likely Case (Based on statistical trends)
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Header Section
st.markdown('<p class="title">🔮 Ibolya AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict Your 10-Year Future with AI</p>', unsafe_allow_html=True)

# User Inputs
career = st.text_input("💼 Enter Your Career Path", placeholder="e.g., AI Researcher, Hedge Fund Manager")
investments = st.text_input("📈 Enter Your Investment Strategy", placeholder="e.g., Crypto, Tech Stocks, Real Estate")
risk_tolerance = st.selectbox("⚖️ Select Your Risk Tolerance", ["Low", "Medium", "High"])

# Prediction Button
if st.button("🔮 See Your Future"):
    if not career or not investments:
        st.warning("⚠️ Please fill out all fields before predicting.")
    else:
        user_data = {"career": career, "investments": investments, "risk_tolerance": risk_tolerance}
        with st.spinner("Analyzing your future..."):
            future_scenarios = get_future_scenarios(user_data)
        st.success("✅ Prediction Complete!")
        st.markdown(f"### 📊 Your 10-Year Forecast:\n\n{future_scenarios}")
