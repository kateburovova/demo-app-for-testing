import streamlit as st

if st.session_state.logged_in:
    st.write('Hi')
else:
    st.write('User not recognised')
