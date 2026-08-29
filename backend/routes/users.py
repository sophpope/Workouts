from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from models import User, UserCreate, UserPublic, UserLogin
from db_utils import SessionDep, engine
from auth import password_hash, verify_password, create_access_token, get_current_user, decode_access_token

router = APIRouter()

def get_user_by_email(email: str, session: Session):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

# showing all user information   
@router.get("/users")
def get_users(session:SessionDep):
    try:
        users = session.exec(select(User)).all()
        return users
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
#creating a new user
@router.post("/create_new_user", response_model=UserPublic)
def create_new_user(user: UserCreate):
    with Session(engine) as session:

        # check if the username or email already exists

        existing_username = session.exec(select(User).where(User.username == user.username)).first()

        if existing_username:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        # check if the email already exists
        existing_email = session.exec(select(User).where(User.email == user.email)).first()

        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = password_hash.hash(user.password)

        db_user = User(
            username=user.username,
            email=user.email,
            password_hash=hashed_password
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
# creating login endpoint

@router.post("/login")
def login(user: UserLogin, session: SessionDep):
    db_user = get_user_by_email(user.email, session)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(db_user.user_id)
    
    return {"message": "Login successful", "user_id": db_user.user_id, "username": db_user.username, "access_token": access_token, "token_type": "bearer"}



# Endpoint to get the current logged-in user's information

@router.get("/me", response_model=UserPublic)
def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

# endpoint for OAuth2 authentication
@router.post("/token")
def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep):
    db_user = get_user_by_email(form_data.username, session)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(db_user.user_id)
    
    return {"access_token": access_token, "token_type": "bearer"}    
