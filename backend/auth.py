import jwt 
from datetime import datetime, timedelta, timezone
#from config import SECRET_KEY, ALGORITHM
from not_for_git_hub import SECRET_KEY, ALGORITHM
from pwdlib import PasswordHash
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, Depends
from models import User
from db_utils import SessionDep
from fastapi.security import OAuth2PasswordBearer


# authentication setup
oauth2_scheme =  OAuth2PasswordBearer(tokenUrl="token")

# setting up password hash 
password_hash = PasswordHash.recommended()

# setting up login functions 
def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(user_id: int):
    expiration = datetime.now(timezone.utc) + timedelta(days=5)
    payload = {"user_id": str(user_id), "exp": expiration}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        user_id = payload.get("user_id")

        if user_id is None:
            raise Exception("Invalid token: user_id not found")
        
        return int(user_id)
    
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
    

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: SessionDep):
    user_id = decode_access_token(token)

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user