#!/usr/bin/env python3

import sys
import os

# Get the absolute path to the directory containing this script (which is 'lib/')
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path to the project root (the parent directory of 'lib/')
project_root_dir = os.path.join(current_script_dir, '..')

# Add the project root to sys.path
sys.path.insert(0, project_root_dir)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.models import Base, Company, Dev, Freebie # <--- This line relies on the above fix!

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Ready for debugging!")
    print("You have access to: session, Company, Dev, Freebie")

    import ipdb; ipdb.set_trace() # Ensure this is AFTER session is defined

    session.close()