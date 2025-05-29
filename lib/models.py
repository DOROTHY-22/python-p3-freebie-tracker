from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Define naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # Establish relationship with Freebie: one Company can have many Freebies
    freebies = relationship('Freebie', backref='company')

    def give_freebie(self, dev, name, value):
        # Method to create a new Freebie instance and associate it with the company and dev
        new_freebie = Freebie(company=self, dev=dev, name=name, value=value)
        return new_freebie

    def __repr__(self):
        return f'<Company {self.name} (Founded: {self.founding_year})>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    # Establish relationship with Freebie: one Dev can receive many Freebies
    freebies = relationship('Freebie', backref='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    value = Column(Integer()) # e.g., points, monetary value

    # Foreign key for Company
    company_id = Column(Integer(), ForeignKey('companies.id'))
    # Foreign key for Dev
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    def __repr__(self):
        return f'<Freebie {self.name} (Value: {self.value}) from {self.company.name} to {self.dev.name}>'