import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit as st

from core import t
from core.state import get_mail_data, reset_mail_data, set_mail_data, switch_sending


def mail_form():
    with st.form(
        key="contact_form",
        enter_to_submit=False,
        clear_on_submit=True,
        border=False,
    ):
        with st.container(horizontal_alignment="center"):
            name = st.text_input(label=f"{t('send_mail.name')} *")
            name_error = st.empty()
            mail = st.text_input(label=t("send_mail.mail"))
            objet = st.text_input(label=f"{t('send_mail.objet')} *")
            objet_error = st.empty()
            msg = st.text_area(label=f"{t('send_mail.msg')} *")
            msg_error = st.empty()
            copie = st.toggle(label="Recevoir une copie")
            if st.form_submit_button(label=t("send_mail.send")):
                errors = 0
                if not name:
                    errors += 1
                    name_error.error("Ajouter un nom avant envoi")
                if not objet:
                    errors += 1
                    objet_error.error("Ajouter un objet avant envoi")
                if not msg:
                    errors += 1
                    msg_error.error("Ajouter un message avant envoi")
                if errors > 0:
                    st.stop()
                set_mail_data(
                    {
                        "name": name,
                        "mail": mail,
                        "objet": objet,
                        "msg": msg,
                        "copie": copie,
                    }
                )
                switch_sending()
                st.rerun()


def generate_mail():
    params = get_mail_data()
    email = MIMEMultipart()
    envoyeur = "jules.chevenetpro@gmail.com"

    full_body = (
        f"Nom : {params['name']}\n"
        f"Email : {params['mail']}\n\n"
        f"Message :\n{params['msg']}\n"
    )
    email = MIMEText(full_body, "plain")
    email["From"] = envoyeur
    receveurs = [envoyeur, params["mail"]] if params["copie"] else [envoyeur]
    email["To"] = ", ".join(receveurs)
    email["Subject"] = params["objet"]
    return email


def send(email):
    app_password = st.secrets["GMAIL_PASSWORD"]
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email["From"], app_password)
        server.sendmail(email["From"], email["To"], email.as_string())


@st.dialog("Envoi en cours")
def sending_mail():
    with st.spinner("En cours d'envoi", show_time=True):
        try:
            mail = generate_mail()
            send(mail)
            st.toast("Envoyé")
        except Exception as e:
            st.toast("Erreur")
            st.toast(e)
    time.sleep(2)
    reset_mail_data()
    switch_sending()
    st.rerun()


@st.dialog(t("send_mail.dialog"))
def send_mail() -> None:
    mail_form()
