import streamlit as st

from composants import fichier_afficheur
from core import t
from objets import Media
from page_model import CustomPage


def home() -> None:
    with st.container(border=True, horizontal=True, vertical_alignment="center", gap="medium"):
        ph: Media = Media("photo.jpeg", "I")
        with st.container(horizontal_alignment="center"):
            fichier_afficheur(ph, 250)
        with st.container():
            st.write(t("home.description.p1"))
            st.write(t("home.description.p2"))
            st.write(t("home.description.p3"))


page: CustomPage = CustomPage(
    name="Jules Chevenet",
    subheader=t("home.description.titre"),
    page_config={
        "page_title": "home.titre",
    },
    page_code=home,
)
page.render()
