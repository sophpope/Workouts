import jwt 
from datetime import datetime, timedelta, timezone
from config import SECRET_KEY, ALGORITHM
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