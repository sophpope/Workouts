import jwt 
from datetime import datetime, timedelta, timezone
#from config import SECRET_KEY, ALGORITHM
from not_for_git_hub import SECRET_KEY, ALGORITHM
from pwdlib import PasswordHash

# setting up password hash 
password_hash = PasswordHash.recommended()

# setting up login functions 
def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(user_id: int):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=30)
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