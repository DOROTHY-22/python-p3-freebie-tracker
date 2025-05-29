#!/usr/bin/env python3

import sys
import os

# Get the absolute path to the directory containing this script (which is 'lib/')
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path to the project root (the parent directory of 'lib/')
project_root_dir = os.path.join(current_script_dir, '..')

# Add the project root to sys.path
sys.path.insert(0, project_root_dir)

# --- You can add these lines for temporary debugging to see what's on your path ---
# print(f"sys.path now includes: {sys.path[0]}")
# print(f"Expected project root: {project_root_dir}")
# ----------------------------------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from lib.models import Base, Company, Dev, Freebie  # Corrected import path

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Deleting old data...")
    
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()
    print("Old data deleted.")

    print("Creating sample companies and devs...")
    # Sample companies here
    apple = Company(name='Apple', founding_year=1971)
    google = Company(name='Google', founding_year=1975)  
    microsoft = Company(name='Microsoft', founding_year=1975)

    # Sample devs here
    esther = Dev(name='Esther')
    bob = Dev(name='Bob')
    reign = Dev(name='Reign')

    session.add_all([apple, google, microsoft, esther, bob, reign])
    session.commit()
    print("Companies and devs created.")
    
    print("Creating sample freebies...")
    # Sample freebies here (using the give_freebie method from Company)
    sticker = apple.give_freebie(esther, 'sticker', 10)
    mug = google.give_freebie(bob, 'mug', 5)
    t_shirt = microsoft.give_freebie(reign, 't-shirt', 3)
    keychain = google.give_freebie(esther, 'keychain', 2) # Added another freebie for Esther
    mousepad = apple.give_freebie(reign, 'mousepad', 8)

    session.add_all([sticker, mug, t_shirt, keychain, mousepad])
    session.commit()
    print("Freebies created.")

    print('Database seeded successfully!')
    session.close()