import pytest
from app import db

@pytest.fixture(autouse=True, scope="module")
def setup_table():
    db.create_table()


def test_connection():
    conn = db.get_connection()
    assert conn is not None
    conn.close()


def test_create():
    result_id = db.insert_result("test_name", "test_value")
    row = db.get_result(result_id)
    assert row[1] == "test_name"
    assert row[2] == "test_value"


def test_update():
    result_id = db.insert_result("to_update", "old_value")
    db.update_result(result_id, "new_value")
    row = db.get_result(result_id)
    assert row[2] == "new_value"


def test_delete():
    result_id = db.insert_result("to_delete", "value")
    db.delete_result(result_id)
    row = db.get_result(result_id)
    assert row is None