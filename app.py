import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="LogiRoute Pro", initial_sidebar_state="collapsed")

# Hide streamlit header and footer to make the app look native
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with open("static/planner.html", "r", encoding="utf-8") as f:
    source_html = f.read()

# Render the HTML directly
components.html(source_html, height=1000, scrolling=True)
