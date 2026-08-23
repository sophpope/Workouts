import jwt 
from datetime import datetime, timedelta, timezone
from config import SECRET_KEY, ALGORITHM
from pwdlib import PasswordHash

# setting up password hash 
password_hash = PasswordHash.recommended()

# setting up login functions 
def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)