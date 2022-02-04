from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

engine = create_engine('sqlite:///tmp/chess.db/', echo=True)

metadata_obj = MetaData()

figures = Table('figures', metadata_obj,
                Column('id', Integer, primary_key=True),
                Column('name', String, nullable=False),
                Column('field', String, nullable=False, unique=True),
                Column('colour', String, nullable=False)
                )

conn = engine.connect()

metadata_obj.create_all(engine)
