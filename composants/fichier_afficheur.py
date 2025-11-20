from io import BufferedReader
from typing import Any

import streamlit as st
from PIL import Image

from objets import MAPPING_FILE_TYPE, Media


def fichier_afficheur(media: Media, width: str | int = "stretch") -> None:
    path: str = media.get_path()
    type: str = media.type
    if type not in MAPPING_FILE_TYPE.keys():
        return
    elif type == "V":
        vid: BufferedReader[Any] = open(path, "rb")
        vid_bytes: bytes = vid.read()
        st.video(vid_bytes, width=width)
    elif type == "I":
        im: Any = Image.open(path)
        st.image(im, width=width)
    elif type == "P":
        st.pdf(path, height=width)
