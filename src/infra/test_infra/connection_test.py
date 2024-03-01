#!/usr/bin/env python3
import pytest
#from sqlalchemy import text
from ..db.settings.connection import DBConnectionHandller

@pytest.mark.skip(reason="Sensitive test")
def test_create_database_engine():
    """test to engine"""
    db_connection_handle = DBConnectionHandller()

    engine = db_connection_handle.get_engine()

    assert engine is not None

    # conn = engine.connect()

    # conn.execute(
    #     text("INSERT INTO users (first_name, last_name, age) VALUES ('test', 'test', 1)")
    # )
    # conn.commit()
    # print(f"\n {engine}")
