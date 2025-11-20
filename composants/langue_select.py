from typing import Any

import streamlit as st

from core import t
from core.state import DICT_LANGUE, DICT_LANGUE_T, get_langue, set_langue


def langue_select() -> None:
    val_langue: str = DICT_LANGUE[get_langue()]

    label: str = "🌐 " + t("langue_select.label")
    options: list[Any] = sorted(DICT_LANGUE.values())
    index: int = options.index(val_langue)

    nv_langue: str = st.selectbox(
        label=label, options=options, index=index, disabled=True
    )  # , width=100

    if nv_langue != val_langue:
        set_langue(DICT_LANGUE_T[nv_langue])
        st.rerun()
