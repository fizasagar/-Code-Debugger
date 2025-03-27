import streamlit as st
import subprocess
import tempfile

def analyze_code(code):
    # Temporary file to store user code
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(code.encode())
        temp_file_path = temp_file.name
    
    # Run Pylint to check for errors
    result = subprocess.run(["pylint", temp_file_path, "--disable=all", "--enable=E"], capture_output=True, text=True)
    return result.stdout

# Streamlit UI
st.title("🐍 Simple Python Code Debugger")
st.write("Paste your Python code below to check for errors!")

code = st.text_area("Enter your Python code:")

if st.button("Check for Errors"):
    if code.strip():
        errors = analyze_code(code)
        st.subheader("🛠️ Debugging Report:")
        st.code(errors if errors else "✅ No errors found!", language="text")
    else:
        st.warning("Please enter some code to analyze.")
