import streamlit as st

# UTILISATION UNIQUEMENT DE CLE

STATE_LANGUE: str = "langue"
DICT_LANGUE: dict[str, str] = {
    "fr": "🇫🇷",
    "en": "🇬🇧",
}
DICT_LANGUE_T: dict[str, str] = {v: k for k, v in DICT_LANGUE.items()}
DEFAUT_CLE_LANGUE: str = "fr"


def init_langue(default: str = DEFAUT_CLE_LANGUE) -> None:
    if STATE_LANGUE not in st.session_state:
        st.session_state[STATE_LANGUE] = default


def get_langue() -> str:
    return str(st.session_state.get(STATE_LANGUE, DEFAUT_CLE_LANGUE))


def set_langue(langue: str) -> None:
    if langue in DICT_LANGUE.keys():
        st.session_state[STATE_LANGUE] = langue


STATE_SENDING = "sending"
DEFAUT_CLE_SENDING = False


def init_sending(default: bool = DEFAUT_CLE_SENDING) -> None:
    if STATE_SENDING not in st.session_state:
        st.session_state[STATE_SENDING] = default


def switch_sending() -> None:
    st.session_state[STATE_SENDING] = not st.session_state[STATE_SENDING]


def get_sending() -> bool:
    return st.session_state[STATE_SENDING]


STATE_MAIL_DATA = "mail_data"
DEFAUT_CLE_MAIL_DATA = None


def reset_mail_data(defaut=DEFAUT_CLE_MAIL_DATA) -> None:
    st.session_state[STATE_MAIL_DATA] = defaut


def init_mail_data() -> None:
    if STATE_MAIL_DATA not in st.session_state:
        reset_mail_data()


def set_mail_data(params) -> None:
    st.session_state[STATE_MAIL_DATA] = params


def get_mail_data() -> dict:
    return st.session_state[STATE_MAIL_DATA]
