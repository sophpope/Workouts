from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from db_utils import SessionDep

# importing user routes
from routes.users import router as users_router

from routes.exercises import router as exercises_router

from routes.workouts import router as workouts_router

# uvicorn main:app --reload (backend)
# npx expo start (frontend)

app = FastAPI()

app.include_router(users_router)
app.include_router(exercises_router)
app.include_router(workouts_router)



# defining the base url for the app
origins = [
    "http://localhost:8081"
]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)






    




