# create_tables.py
from app.db.session import engine
from app.db.base import Base

# create all tables defined on Base subclasses
Base.metadata.create_all(bind=engine)
print("✅ Tables created!")
