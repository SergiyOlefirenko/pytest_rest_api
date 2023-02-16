from src.DAL.dvdrental.tables import Film, Language
from datetime import datetime


def test_get_films_data(get_db_session):
    data = get_db_session.query(Film).first()
    print(data.film_id, data.title)


def test_try_to_insert_language(get_db_session, get_add_method):
    new_lang = {"name": "Ukrainian", "last_update": datetime.now()}
    lang = Language(**new_lang)
    get_add_method(get_db_session, lang)

    u_lang = get_db_session.query(Language).filter(Language.name == new_lang["name"]).one_or_none()
    print(u_lang.name, u_lang.language_id)


def test_try_to_delete_language(get_db_session, get_delete_method):
    rows = get_delete_method(get_db_session, Language, (Language.name == 'Ukrainian'))
    print(f'Rows deleted: {rows}.')


def test_insert_with_language_builder(get_db_session, get_add_method, get_lang_builder):
    lang = Language(**get_lang_builder.build())
    get_add_method(get_db_session, lang)
    print(f'Generated lang id : {lang.language_id}, name: {lang.name}.')


def test_combined_fixed_for_insert_delete(generate_test_language):
    print(f'Generated lang id : {generate_test_language.language_id}, name: {generate_test_language.name}.')
