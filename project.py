import streamlit as st
import ast

# Custom CSS for theme colors
st.markdown("""
    <style>
        body {
            background-color: #a7d1f9;
            color: #4138f3;
        }
        .stApp {
            background-color: #a7d1f9;
        }
        .stButton>button {
            background-color: #27548A;
            color: white;
        }
        .stTextInput>div>div>input {
            border-color: #4138f3;
        }
    </style>
""", unsafe_allow_html=True)

#  Streamlit UI Setup
st.title("🐍 AI-Powered Code Debugger")
st.write("Paste your Python code below and click 'Debug' to find errors! 🛠️")

#  User input area
code = st.text_area("Enter Python Code:", height=200)

def analyze_code(code):
    try:
        # 🌱 Parsing code to check syntax
        ast.parse(code)
        return "✅ No syntax errors found! Your code looks good."
    except SyntaxError as e:
        return f"❌ Syntax Error: {e.msg} at line {e.lineno}"
    except Exception as e:
        return f"⚠️ Other Error: {str(e)}"

#  Debug button
if st.button("Debug Code"):
    if code.strip():
        result = analyze_code(code)
        st.code(result)
    else:
        st.warning("⚠️ Please enter some code to debug!")
