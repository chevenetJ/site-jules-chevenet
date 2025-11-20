from typing import Callable

import streamlit as st

from composants import langue_select
from core import t
from core.state import init_langue, init_mail_data, init_sending

global_page_config: dict[str, str | None] = {
    "page_icon": None,
    "layout": "centered",
    "initial_sidebar_state": "auto",
    "menu_items": None,
}


def defaut_page_code() -> None:
    st.write("En construction")


def init_state() -> None:
    init_langue()
    init_sending()
    init_mail_data()


class CustomPage:
    def __init__(
        self,
        name: str,
        subheader: str,
        page_config: dict[str, str] = {
            "page_title": "En construction",
        },
        page_code: Callable[[], None] = defaut_page_code,
    ):
        self.name = name
        self.subheader = subheader
        self.page_config = {**page_config, **global_page_config}
        self.page_code = page_code
        init_state()

    def set_page_config(self) -> None:
        page_title = t(self.page_config["page_title"])
        st.set_page_config(
            page_title=page_title,
            page_icon=self.page_config["page_icon"],
            layout=self.page_config["layout"],
            initial_sidebar_state=self.page_config["initial_sidebar_state"],
            menu_items=self.page_config["menu_items"],
        )

    def header(self) -> None:
        with st.container(horizontal=True, vertical_alignment="center"):
            with st.container(horizontal_alignment="left"):
                st.header(self.subheader)
            with st.container(horizontal_alignment="right", width=100):
                langue_select()

    def render(self) -> None:
        self.set_page_config()
        self.header()
        self.page_code()
