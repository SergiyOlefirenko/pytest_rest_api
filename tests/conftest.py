import pytest
from random import randrange
from src.generators.player import Player
from src.generators.language import Language

from src.DAL.db import Session
from src.DAL.dvdrental import tables


@pytest.fixture
def get_player_generator():
    return Player()


# this fixture will be accessible from both tests folders ('users' and 'something')
@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


# --> function and that will be returned by fixture
def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None

@pytest.fixture
def calculate():
    return _calculate
# <-- function and that will be returned by fixture


# setup and teardown fixtures
@pytest.fixture
def make_number():
    print("\nI'm getting number.")
    number = randrange(1, 1000, 5)
    yield number
    print(f"\nNumber at home {number}")


# --> db fixtures sqlalchemy
@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    except:
        session.close()

def delete_test_data(session, table, filter_data):
    number_of_deleted_rows = session.query(table).filter(filter_data).delete()
    session.commit()
    return number_of_deleted_rows

def add_method(session, item):
    session.add(item)
    session.commit()

@pytest.fixture
def get_delete_method():
    return delete_test_data

@pytest.fixture
def get_add_method():
    return add_method

@pytest.fixture
def get_lang_builder():
    return Language()

@pytest.fixture
def generate_test_language(get_db_session, get_lang_builder, get_add_method, get_delete_method):
    lang = tables.Language(**get_lang_builder.build())
    get_add_method(get_db_session, lang)
    yield lang
    get_delete_method(get_db_session, tables.Language, (tables.Language.language_id == lang.language_id))
# <-- db fixtures sqlalchemy