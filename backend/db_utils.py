from sqlmodel import SQLModel, Session, create_engine
#from config import DATABASE_URL
from not_for_git_hub import DATABASE_URL
from typing import Annotated
from fastapi import Depends

database_url = DATABASE_URL

engine = create_engine(database_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
