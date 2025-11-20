MAPPING_FILE_TYPE = {"V": "video", "I": "photo", "P": "pdf"}


class Media:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def get_path(self) -> str:
        return f"fichiers/{MAPPING_FILE_TYPE[self.type]}/{self.name}"
