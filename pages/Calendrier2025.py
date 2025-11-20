from datetime import date

import streamlit as st

from page_model import CustomPage

topics = [
    {"date": date(2025, 12, 1), "name": "Le marché des calendriers de Noël"},
    {"date": date(2025, 12, 2), "name": "Le marché des calendriers de Noël"},
    {"date": date(2025, 12, 3), "name": "Le marché des calendriers de Noël"},
    {"date": date(2025, 12, 4), "name": "Le marché des calendriers de Noël"},
    {"date": date(2025, 12, 5), "name": "Le marché des calendriers de Noël"},
    {"date": date(2025, 12, 6), "name": "Le marché des calendriers de Noël"},
]


def today_topic():
    with st.container(border=True):
        with st.container(horizontal=True, vertical_alignment="center"):
            st.write("Aujourd'hui :")
            st.button(label="1 - Le marché des calendriers de Noël")


def search_topic():
    with st.container(
        border=True,
    ):
        st.text_input(label="Rechercher", placeholder="mots clés ...")
        st.expander("Plus de filtres")


def render_topic(topic):
    with st.container(vertical_alignment="center", border=True):
        st.write(f"{topic['date'].day} - {topic['name']}")
        with st.container(horizontal=True):
            st.button(label="Plus d'infos", key=f"{str(topic['date'].day)}_info")
            st.button(label="Accéder", key=f"{str(topic['date'].day)}_go")


def render_topics(topics):
    with st.container(
        horizontal=True,
    ):
        for topic in topics:
            render_topic(topic)


def calendrier2025():
    st.sidebar.divider()
    st.sidebar.page_link("pages/Calendrier2025.py", label="Accueil Calendrier 2025")
    with st.container(border=True):
        today_topic()
        st.write("Bienvenue sur le calendrier de l'Avant Data de Jules Chevenet !")
        search_topic()
        render_topics(topics)


page: CustomPage = CustomPage(
    name="Calendrier2025",
    subheader="Accueil Calendrier 2025",
    # page_config={
    #    "page_title": "home.titre",
    # },
    page_code=calendrier2025,
)
page.render()
