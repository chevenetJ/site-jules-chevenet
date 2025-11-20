import streamlit as st

# UTILISATION UNIQUEMENT DE CLE

STATE_LANGUE: str = "langue"
DICT_LANGUE: dict = {
    "fr": "🇫🇷",
    "en": "🇬🇧",
}
DICT_LANGUE_T: dict = {v: k for k, v in DICT_LANGUE.items()}
DEFAUT_CLE_LANGUE: str = "fr"


def init_langue(default: str = DEFAUT_CLE_LANGUE) -> None:
    if STATE_LANGUE not in st.session_state:
        st.session_state[STATE_LANGUE] = default


def get_langue() -> str:
    return st.session_state.get(STATE_LANGUE, DEFAUT_CLE_LANGUE)


def set_langue(langue: str) -> None:
    if langue in DICT_LANGUE.keys():
        st.session_state[STATE_LANGUE] = langue


STATE_SENDING = "sending"
DEFAUT_CLE_SENDING = False


def init_sending(default: bool = DEFAUT_CLE_SENDING):
    if STATE_SENDING not in st.session_state:
        st.session_state[STATE_SENDING] = default


def switch_sending():
    st.session_state[STATE_SENDING] = not st.session_state[STATE_SENDING]


def get_sending():
    return st.session_state[STATE_SENDING]


STATE_MAIL_DATA = "mail_data"
DEFAUT_CLE_MAIL_DATA = None


def reset_mail_data(defaut=DEFAUT_CLE_MAIL_DATA):
    st.session_state[STATE_MAIL_DATA] = defaut


def init_mail_data():
    if STATE_MAIL_DATA not in st.session_state:
        reset_mail_data()


def set_mail_data(params):
    st.session_state[STATE_MAIL_DATA] = params


def get_mail_data():
    return st.session_state[STATE_MAIL_DATA]
