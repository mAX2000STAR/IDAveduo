
import streamlit as st

def main_page():
    st.markdown("# الرخصه الزهبيه ")
    st.sidebar.markdown("# الرخصه الزهبيه ")
    st.video("alrhsa alzhpeh.mp4")
def page2():
    st.markdown("# قانون الحمايه")
    st.sidebar.markdown("# قانون الحمايه")
    st.video("kanoon alhmaeh.mp4")
def page3():
    st.markdown("# المثتثمر الاجنبي")
    st.sidebar.markdown("# المثتثمر الاجنبي")
    st.video("almstsmr.mp4")
page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
