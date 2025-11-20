from datetime import date

from core import t
from objets import Media, Projet

prj_cal: Projet = Projet(
    name=t("prj.cal.name"),
    date=(date(2025, 12, 1), None),
    description=t("prj.cal.description"),
    # link = "Calendrier2025"
)
prj_ffbb: Projet = Projet(
    name=t("prj.ffbb.name"),
    date=(date(2023, 8, 1), None),
    description=t("prj.ffbb.description"),
    link="https://app-ffbb.streamlit.app/",
)
prj_sncf: Projet = Projet(
    name=t("prj.sncf.name"),
    date=(date(2022, 8, 1), None),
    description=t("prj.sncf.description"),
    link="https://chevenetj-app-sncf-streamlit-01-visualisation-98ikkv.streamlit.app/",
)

PROJET_PERSO: list[Projet] = [prj_cal, prj_ffbb, prj_sncf]

v_data_jo: str = "video_pres_JO.mp4"

prj_jo: Projet = Projet(
    name=t("prj.jo.name"),
    date=(date(2023, 9, 1), None),
    description=t("prj.jo.description"),
    medias=[Media(v_data_jo, "V")],
)

PROJET_PRO: list[Projet] = [prj_jo]

v_data_taw_1_data: str = "TAW_pres.mp4"
v_data_taw_2_data: str = "pitch.mp4"
v_data_clu: str = "26_le_clustering_video.mp4"

prj_taw: Projet = Projet(
    name=t("prj.taw.name"),
    date=(date(2020, 11, 1), date(2021, 5, 1)),
    description=t("prj.taw.description"),
    medias=[Media(v_data_taw_1_data, "V"), Media(v_data_taw_2_data, "V")],
)
prj_jo_scol: Projet = Projet(
    name=t("prj.jo_scol.name"),
    date=(date(2020, 11, 1), None),
    description=t("prj.jo_scol.description"),
    link="https://rdashboardesiee.shinyapps.io/app-1/",
)
prj_clu: Projet = Projet(
    name=t("prj.clu.name"),
    date=(date(2020, 5, 1), date(2020, 6, 1)),
    description=t("prj.clu.description"),
    medias=[Media(v_data_clu, "V")],
)

PROJET_SCO: list[Projet] = [prj_taw, prj_jo_scol, prj_clu]
