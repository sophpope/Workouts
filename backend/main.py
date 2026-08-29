from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlmodel import Session, select, Field, SQLModel, create_engine
from sqlalchemy import text
from db_utils import engine 
from models import User, Exercise, WorkoutExercise, Set, PersonalRecords, Workout, UserCreate, ExerciseCreate, WorkoutExerciseCreate, SetCreate, PersonalRecordsCreate, WorkoutCreate, UserPublic, ExercisePublic, WorkoutExercisePublic, SetPublic, PersonalRecordsPublic, WorkoutPublic, newWorkout, newWorkoutExercise, newSetCreate, UserLogin
from typing import Annotated, List
from datetime import datetime, timezone, timedelta
from auth import get_current_user
from db_utils import SessionDep

# importing user routes
from routes.users import router as users_router

from routes.exercises import router as exercises_router

# uvicorn main:app --reload (backend)
# npx expo start (frontend)

app = FastAPI()

app.include_router(users_router)
app.include_router(exercises_router)



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





    
# Create a new workout 
@app.post("/create_workout", response_model=WorkoutPublic)
def create_workout(
    workout: WorkoutCreate,
    session:SessionDep,
    current_user: Annotated[User, Depends(get_current_user)]):

    db_workout = Workout.model_validate(workout, update={"user_id": current_user.user_id})

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



