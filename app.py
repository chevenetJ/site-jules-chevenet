import streamlit as st

rooter = st.navigation(
    pages=[
        "pages/01_Jules_Chevenet.py",
        "pages/02_Projets.py",
        "pages/03_Contact.py",
        # "pages/Calendrier2025.py",
    ],
    position="hidden",
)

st.sidebar.page_link("pages/01_Jules_Chevenet.py")
st.sidebar.page_link("pages/02_Projets.py")
st.sidebar.page_link("pages/03_Contact.py")

rooter.run()
