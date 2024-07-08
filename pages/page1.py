import streamlit as st

try:
    if st.session_state.logged_in:
        st.write('Hi')
    else:
        st.write('User not recognised')
except Exception as e:
    "You are not authorised to visit this page"
