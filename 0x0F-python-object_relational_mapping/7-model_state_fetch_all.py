#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    active_session = sessionmaker(bind=engine)
    mySession = active_session()
    myquery = mySession.query(State).order_by(State.id)

    for row in myquery:
        print("{}: {}".format(row.id, row.name))
