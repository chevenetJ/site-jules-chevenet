from datetime import date

from objets import Media


class Projet:
    def __init__(
        self,
        name: str | None = None,
        date: tuple[date, date | None] = None,
        description: str | None = None,
        link: str | None = None,
        medias: list[Media] | None = None,
    ):
        self.name = name
        self.date = date
        self.description = description
        self.link = link
        self.medias = medias
