import streamlit as st
import streamlit.components.v1 as components

try:
    if st.session_state.logged_in:
        st.write('Hi')
        kibana_url = st.secrets['KIBANA_DASHBOARD_URL']
        components.iframe(kibana_url, height=600, scrolling=True)
    else:
        st.write('User not recognised')
except Exception as e:
    "You are not authorised to visit this page"
    

