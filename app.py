import streamlit as st
import streamlit.components.v1 as components

# from st_supabase_connection import SupabaseConnection
#
# st.write('This is a test app')
#
# st_supabase_client = st.connection(
#     name="demo-streamlit-connection",
#     type=SupabaseConnection,
#     ttl=None)
#
# email = st.text_input("Enter email")
# password = st.text_input("Enter password", type="password")
#
# if st.button("Log in", type="primary"):
#     try:
#         st_supabase_client.auth.sign_in_with_password(dict(email=email, password=password))
#         st.session_state.logged_in = True
#         st.success(f"Logged in as {email}")
#         st.switch_page("pages/page1.py")
#     except Exception as e:
#         st.error(f"There is an issue with your credentials: ({e}).\nPlease try again.")
#
# kibana_url = st.secrets['KIBANA_DASHBOARD_URL']
# components.iframe(kibana_url, height=600, scrolling=True)
looker_url = st.secrets['LOOKER_DASHBOARD_URL']
components.iframe(looker_url, height=600, scrolling=True)
