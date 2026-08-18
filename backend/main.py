from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import Session, select, Field, SQLModel, create_engine
from sqlalchemy import text
from db_utils import engine 
from models import User, Exercise, WorkoutExercise, Set, PersonalRecords, Workout, UserCreate, ExerciseCreate, WorkoutExerciseCreate, SetCreate, PersonalRecordsCreate, WorkoutCreate, UserPublic, ExercisePublic, WorkoutExercisePublic, SetPublic, PersonalRecordsPublic, WorkoutPublic, newWorkout, newWorkoutExercise, newSetCreate, UserLogin
from typing import Annotated, List
from datetime import datetime, timezone
from pwdlib import PasswordHash

# setting up password hash 
password_hash = PasswordHash.recommended()

# setting up login functions 
def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def get_user_by_email(email: str, session: Session):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

# uvicorn main:app --reload
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

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

# @app.get("/test-db")
# def test_db():
#     try:
#         with Session(engine) as session:
#             result = session.exec(text("SELECT 1")).one()
#             return {"status": "connected", "result": result[0]}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}


@app.get("/test-db")
def test_db(session: SessionDep):
    try:
        result = session.exec(text("SELECT 1")).one()
        return {"status": "connected", "result": result[0]}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# showing all user information   
@app.get("/users")
def get_users(session:SessionDep):
    try:
        users = session.exec(select(User)).all()
        return users
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
#creating a new user
@app.post("/create_new_user", response_model=UserPublic)
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

# Returning specific exercise info for crow pose
@app.get("/exercises_specific")
def get_specifc_exercise(session:SessionDep):
    try:
        exercise = select(Exercise).where(Exercise.exercise_name == "L Sit")
        exercises = session.exec(exercise).first()
        return exercises
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Exercise {exercise} not found")

@app.get("/exercises")
def get_exercises(session:SessionDep):
    try:
        exercises = session.exec(select(Exercise)).all()
        return exercises
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
#Trying with an exercise that is not in the database, to see if my HTTPException works
@app.get("/exercises_test")
def not_exercise(session:SessionDep):
    try:
        test_exercise = select(Exercise).where(Exercise.exercise_name == "Dips")
        dips = session.exec(test_exercise).first()
        if not test_exercise:
            raise HTTPException(status_code=404, detail=f"Exercise {test_exercise} not found")
        return dips
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code Error")

# Create a new exercise request
@app.post("/create_exercise", response_model=ExercisePublic)
def create_exercise(exercise: ExerciseCreate):
    with Session(engine) as session:
        db_exercise = Exercise.model_validate(exercise)
        session.add(db_exercise)
        session.commit()
        session.refresh(db_exercise)
        return db_exercise
    
# Create a new workout 
@app.post("/create_workout", response_model=WorkoutPublic)
def create_workout(workout: WorkoutCreate, session:SessionDep):
    db_workout = Workout.model_validate(workout)
    session.add(db_workout)
    session.commit()
    session.refresh(db_workout)
    return db_workout

# Viewing workouts
@app.get("/get_workout")
def get_workouts(session:SessionDep):
    try:
        exercises = session.exec(select(Exercise)).all()
        return exercises
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Route to add a whole new workout, with the exercise and set
@app.post("/new_workout")
def create_workout(
    workout: WorkoutCreate,
    workout_exercise: newWorkoutExercise,
    sets: newSetCreate,
    session: SessionDep
):
    new_workout = Workout.model_validate(workout)
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)

    
    for workout_exercise in new_workout:
        new_workout_exercise = WorkoutExercise.model_validate(
        workout_exercise,
        update = {"workout_id": new_workout.workout_id})
        session.add(new_workout_exercise)
        session.commit()
        session.refresh(new_workout_exercise)

    
        for sets in new_workout_exercise:
            new_set = Set.model_validate(
            sets,
            update = {"workout_exercise_id": new_workout_exercise.workout_exercise_id})
            session.add(new_set)
            session.commit()
            session.refresh(new_set)

    return {
        "workout": new_workout,
        "workout_exercise": new_workout_exercise,
        "set": new_set
        
    }

# creating login endpoint

@app.post("/login")
def login(user: UserLogin, session: SessionDep):
    db_user = get_user_by_email(user.email, session)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "user_id": db_user.user_id, "username": db_user.username}