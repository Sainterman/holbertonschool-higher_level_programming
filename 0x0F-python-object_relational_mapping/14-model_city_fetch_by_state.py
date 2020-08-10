#!/usr/bin/python3
"""Create engine, session and query the state table"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """DO IT! Create engine, list first state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).\
        filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
