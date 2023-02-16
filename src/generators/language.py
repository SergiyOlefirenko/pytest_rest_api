from faker import Faker
from datetime import datetime


class Language():

    fake = Faker()

    def __init__(self) -> None:
        self.result = {}
        self.reset()

    def set_language(self, lang=fake):
        if not isinstance(lang, str):
            lang = lang.currency()[1]
            self.result['name'] = lang if len(lang) < 21 else lang[:20]
        else:
            self.result['name'] = lang
        self.result['last_update'] = datetime.now()
        return self

    def reset(self):
        self.set_language()
        return self

    def build(self):
        return self.result


if __name__ == '__main__':
    pass