#!/usr/bin/python3
"""
 lists all State objects, and corresponding City
 objects, contained in the database hbtn_0e_101_usa
"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    new_state = State(name='Louisiana')
    local_session.add(new_state)
    local_session.commit()

    print(new_state.id)
    local_session.close()
    engine.dispose()
