from src.DAL.db import Session
from src.DAL.dvdrental import tables
from sqlalchemy.sql.expression import desc
from sqlalchemy import insert
from datetime import datetime
from faker import Faker

# session = Session()

# result = session.query(
#     tables.Film.film_id,
#     tables.Film.title,
#     tables.Film.replacement_cost
# ).filter(
#     tables.Film.film_id < 10, tables.Film.replacement_cost > 20
# ).order_by(desc(tables.Film.film_id)).limit(3).all()

# print(result)

# langs = session.query(tables.Language).all()
# print(f'Count of langs before insert: {len(langs)}')
# stmt = (
#     insert(tables.Language).values(name='Ukrainian', last_update=datetime.now())
# )
# session.execute(statement=stmt)
# session.commit()

# langs = session.query(tables.Language).all()
# print(f'Count of langs after insert: {len(langs)}')

# o = session.query(tables.Language).filter(tables.Language.name == 'Ukrainian').delete()
# print(o)
# session.commit()

# langs = session.query(tables.Language).all()
# print(f'Count of langs after delete: {len(langs)}')

# session.close()

fake = Faker()
for _ in range(5):
    print(fake.currency()[1])

class Lang():

    def __init__(self) -> None:
        self.result = {}
        self.reset()

    def set_currency(self, currency=fake):
        if not isinstance(currency, str):
            self.result['currency'] = currency.currency()[1]
        else:
            self.result['currency'] = currency
        return self

    def reset(self):
        self.set_currency()

    def build(self):
        return self.result

l1 = Lang()
print(f'l1 result: {l1.result}')
l1 = l1.set_currency(currency='Hryvna').build()
l2 = Lang().build()

print(f'l1: {l1}\nl2: {l2}')

