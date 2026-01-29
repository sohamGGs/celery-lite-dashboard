import time
import random
from models import Session, Task
from sqlalchemy import asc
from datetime import datetime

def process_tasks():
    print("Worker started... waiting for tasks.")
    while True:
        session = Session()
        try:
            # Lock the row
            task = session.query(Task).filter_by(status='PENDING')\
                .order_by(asc(Task.created_at))\
                .with_for_update().first()

            if task:
                task.status = 'PROCESSING'
                session.commit()
                
                print(f"Processing: {task.task_name}")
                # Simulate heavy work
                time.sleep(random.randint(3, 8)) 
                
                task.status = 'COMPLETED'
                task.updated_at = datetime.now()
                session.add(task)
                session.commit()
            else:
                session.rollback()
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            session.rollback()
        finally:
            session.close()

if __name__ == "__main__":
    process_tasks()