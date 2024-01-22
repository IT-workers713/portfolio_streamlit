import streamlit as st

from myemail import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("enter email ")
    message = st.text_area("enter message")
    message = message + "\n" + user_email
    button = st.form_submit_button("submit")

    if button:
       send_email(message)
