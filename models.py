from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///tasks.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task_name = Column(String, nullable=False)
    status = Column(String, default='PENDING') 
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.task_name,
            "status": self.status,
            "time": self.created_at.strftime("%H:%M:%S")
        }

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("DB Initialized.")