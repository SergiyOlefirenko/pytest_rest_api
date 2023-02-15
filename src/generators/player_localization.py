from faker import Faker


class PlayerLocalization():

    def __init__(self, lang) -> None:
        self.fake = Faker(locale=lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def build(self):
        return self.result
