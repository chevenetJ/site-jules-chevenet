import streamlit as st

from composants import fichier_afficheur, send_mail, sending_mail
from core import t
from core.state import get_sending
from objets import Media
from page_model import CustomPage

linkedIn_link = "https://www.linkedin.com/in/jules-chevenet-4441b4189/"
linkedIn_label = "LinkedIn"
mail = "jules.chevenet.pro@gmail.com"
tel = "+33 777 38 24 51"
CV = Media("CV Jules Chevenet.pdf", "P")


def contact() -> None:
    with st.container(
        border=True,
        horizontal=True,
        vertical_alignment="distribute",
        horizontal_alignment="center",
    ):
        with st.container(border=True, vertical_alignment="center"):
            st.write(f"📱 Téléphone : {tel}")
            st.write(f"📧 Mail : {mail}")
            st.write("📍 Localisation : Paris, France")
        with st.container(vertical_alignment="center"):
            st.link_button(
                label=linkedIn_label,
                url=linkedIn_link,
                icon=None,
                use_container_width=True,
            )
            if st.button(label=t("contact.contact_button"), use_container_width=True):
                send_mail()
            elif get_sending():
                sending_mail()
            with open(CV.get_path(), "rb") as f:
                pdf_bytes = f.read()
            st.download_button(
                label=t("contact.dl_CV_button"),
                data=pdf_bytes,
                file_name=CV.name,
                mime="application/pdf",
                use_container_width=True,
            )
    fichier_afficheur(CV)


page: CustomPage = CustomPage(
    name="Contact",
    subheader=t("contact.subheader"),
    page_config={
        "page_title": "contact.titre",
    },
    page_code=contact,
)
page.render()
