#!/usr/bin/python3
""" Start link class to table in database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """ Connect and Read Data Base """
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3],
                                                     pool_pre_ping=True)

    engine = create_engine(db)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    records = session.query(State)

    for record in records:
        print('{}: {}'.format(record.id, record.name))
        for _record in record.cities:
            print('\t{}: {}'.format(_record.id, _record.name))

    session.close()


if __name__ == "__main__":
    main()
