from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class DBConnectionHandller:
    """Class to connection to MySql"""

    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            'root',
            'localhost',
            '3306',
            'dmarket_database'
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self: object):
        """return engine database"""
        return self.__engine

    def __enter__(self: object):
        session_make = sessionmaker(bind= self.__engine)
        self.session = session_make()
        return self

    def __exit__(self: object, exc_type, exc_val, exc_tb):
        self.session.close()
        return self
