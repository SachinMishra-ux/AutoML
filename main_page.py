import streamlit as st

def main_page():
    st.markdown("# Welcome to AutoML world!! ð")
    st.sidebar.markdown("# Main page ð")

def classification():
    st.markdown("# Classification is defined as the process of recognition, understanding, and grouping of objects and ideas into preset categories a.k.a âsub-populations. âï¸")
    st.sidebar.markdown("# Classification âï¸")

def regression():
    st.markdown("# Regression is a statistical method used in finance, investing, and other disciplines that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y) and a series of other variables (known as independent variables)  ð")
    st.sidebar.markdown("Regression ð ")

page_names_to_funcs = {
    "Main Page": main_page,
    "Classification": classification,
    "Regression": regression,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()