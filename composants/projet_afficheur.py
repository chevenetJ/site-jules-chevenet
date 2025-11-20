import streamlit as st

from composants.fichier_afficheur import fichier_afficheur
from core import t, t_date
from objets import Projet


def projet_afficheur(projet: Projet) -> None:
    with st.expander(label=f"**{projet.name}** - {t_date(projet.date)}", expanded=False):
        with st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="center"):
            with st.container():
                st.write(projet.description)
            if projet.link is not None:
                with st.container():
                    st.link_button(
                        url=projet.link,
                        label=t("projet.afficheur.link.label"),
                        icon=None,
                        use_container_width=True,
                    )
            if projet.medias is not None:
                with st.container():
                    for media in projet.medias:
                        fichier_afficheur(media)
