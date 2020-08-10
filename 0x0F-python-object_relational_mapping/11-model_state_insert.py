#!/usr/bin/python3
"""Create engine, session and query the state table"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """DO IT! Create engine, list all states ordered by id"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    newState = session.query(State).filter(State.name == "Louisiana").first()
    print(newState.id)
    session.commit()
    session.close()
