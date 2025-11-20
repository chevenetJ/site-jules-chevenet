import json
from datetime import date
from typing import Any

from babel.dates import format_date

from core.state import DEFAUT_CLE_LANGUE, get_langue

_cache: dict = {}


def load_trad(langue: str) -> dict:
    if langue in _cache:
        return _cache[langue]

    path: str = f"i18n/{langue}.json"
    with open(path, "r", encoding="utf-8") as f:
        data: Any = json.load(f)

    _cache[langue] = data
    return data


def t(cle: str) -> str:
    langue: str = get_langue()
    data: dict = load_trad(langue)

    if cle in data:
        return data[cle]

    defaut: dict = load_trad(DEFAUT_CLE_LANGUE)
    return defaut.get(cle, f"??{cle}??")


def t_date(date: tuple[date | None]) -> str:
    langue: str = get_langue()
    d1, d2 = date
    s1 = format_date(d1, "MMM y", locale=langue)
    if not d2:
        return s1
    return f"{s1} - {format_date(d2, 'MMM y', locale=langue)}"
