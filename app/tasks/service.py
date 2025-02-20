from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.tasks.models import Task
from app.tasks.schemas import TaskCreate, TaskUpdate

class TaskService:
    no_task:str = "Task doesn't exits"
    # CREATE
    # ----------------------
    def create_task(self, item_data: TaskCreate, session: SessionDep):
        task_db = Task.model_validate(item_data.model_dump())
        session.add(task_db)
        session.commit()
        session.refresh(task_db)
        return task_db

    # GET ONE
    # ----------------------
    def get_task(self, item_id: int, session: SessionDep):
        task_db = session.get(Task, item_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return task_db

    # UPDATE
    # ----------------------
    def update_task(self, item_id: int, item_data: TaskUpdate, session: SessionDep):
        task_db = session.get(Task, item_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        task_db.sqlmodel_update(item_data_dict)
        session.add(task_db)
        session.commit()
        session.refresh(task_db)
        return task_db

    # GET ALL PLANS
    # ----------------------
    def get_tasks(self, session: SessionDep):
        return session.exec(select(Task)).all()

    # DELETE
    # ----------------------
    def delete_task(self, item_id: int, session: SessionDep):
        task_db = session.get(Task, item_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(task_db)
        session.commit()
        print("debería salir el mensaje")
        return {"detail": "ok"}
