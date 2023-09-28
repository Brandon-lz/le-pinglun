from typing import Optional

from sqlmodel import Field, Session, SQLModel, select
from db import get_engine

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    remark_name: str
    content: Optional[str] = Field(default='')



async def create_comment(remark_name:str,content:str):
    comment = Comment(remark_name=remark_name,content=content)
    with Session(get_engine()) as session:
        session.add(comment)
        session.commit()


async def list_comments()->list:
    with Session(get_engine()) as session:
        statement = select(Comment)
        comments = session.exec(statement).all()
        return comments
    

async def get_comment_by_remark_name(remark_name:str)->str:
    with Session(get_engine()) as session:
        statement = select(Comment).where(Comment.remark_name == remark_name)
        comments = session.exec(statement).all()
        return comments


async def delete_comment(remark_name:str):
    with Session(get_engine()) as session:
        statement = select(Comment).where(Comment.remark_name == remark_name)
        results = session.exec(statement)
        for cm in results:
            session.delete(cm)
        session.commit()
        
