import streamlit as st

from composants import projet_afficheur
from core import t
from page_model import CustomPage
from pages import PROJET_PERSO, PROJET_PRO, PROJET_SCO


def projet() -> None:
    with st.container(border=True):
        st.write(
            "Voici différents projets que j'ai réalisé, catégorisés en trois partie (personnels, professionels, scolaires) et triés du plus récent au plus ancien."
        )
        st.divider()
        st.subheader("Personnels")
        for projet in PROJET_PERSO:
            projet_afficheur(projet)
        st.divider()
        st.subheader("Professionels")
        for projet in PROJET_PRO:
            projet_afficheur(projet)
        st.divider()
        st.subheader("Scolaires")
        for projet in PROJET_SCO:
            projet_afficheur(projet)


page = CustomPage(
    name="Projet",
    subheader=t("projet.subheader"),
    page_config={
        "page_title": "projet.titre",
    },
    page_code=projet,
)
page.render()
