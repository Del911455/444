import streamlit as st

# Page configuration
st.set_page_config(page_title="Publishers Clearing House Login", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        .pch-header {
            background-color: #003087;
            padding: 1.5rem;
            color: white;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            position: relative;
            border-radius: 0px 0px 8px 8px;
        }
        .pch-header img {
            max-width: 150px; /* Reduced size to fit within the header */
            height: auto;
            vertical-align: middle;
        }
        .fdic-box {
            background-color: #f5f5f5;
            padding: 1rem;
            margin: 1.5rem 0;
            border-radius: 8px;
            text-align: center;
            font-size: 14px;
        }
        .login-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .show-password {
            font-size: 12px;
            color: #003087;
            text-align: right;
            margin-top: -10px;
            margin-bottom: 10px;
        }
        .checkbox-label {
            font-size: 14px;
            margin-left: 8px;
        }
        .security-info {
            text-align: center;
            margin-top: 2rem;
            color: gray;
            font-size: 13px;
        }
        .login-button {
            background-color: #003087;
            color: white;
            border: none;
            padding: 0.75rem;
            width: 100%;
            font-size: 16px;
            border-radius: 4px;
        }
        .link-style {
            color: #003087;
            font-size: 13px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header with PCH logo
st.markdown('<div class="pch-header"><img src="pch_logo.png" alt="Publishers Clearing House Logo"></div>', unsafe_allow_html=True)

# FDIC box
st.markdown('<div class="fdic-box">FDIC-Insured - Backed by the full faith and credit of the U.S. Government.</div>', unsafe_allow_html=True)

# Login form
st.markdown('<div class="login-title">Account Login</div>', unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
st.markdown('<div class="show-password">🔒 Show</div>', unsafe_allow_html=True)

# Remember username
remember = st.checkbox("Remember my username")

# Login button
st.markdown('<button class="login-button">Log In</button>', unsafe_allow_html=True)

# Links
st.markdown("""
<div class="link-style">
    <a href="#">Forgot username or password?</a><br>
    <a href="#">Enroll in online banking</a>
</div>
""", unsafe_allow_html=True)

# Security notice
st.markdown('<div class="security-info">🔒 Connection Secured</div>', unsafe_allow_html=True)
