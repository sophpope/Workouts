from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from models import Workout, WorkoutCreate, WorkoutPublic, WorkoutExercise, WorkoutExerciseCreate, Exercise, ExerciseCreate, User, Set, SetCreate
from db_utils import SessionDep
from auth import get_current_user

router = APIRouter()

# Create a new workout 
@router.post("/create_workout", response_model=WorkoutPublic)
def create_workout(
    workout: WorkoutCreate,
    session:SessionDep,
    current_user: Annotated[User, Depends(get_current_user)]):

    db_workout = Workout.model_validate(workout, update={"user_id": current_user.user_id})

    session.add(db_workout)
    session.commit()
    session.refresh(db_workout)
    return db_workout

# Viewing workouts for logged in user
@router.get("/get_workout")
def get_workouts(session:SessionDep, current_user: Annotated[User, Depends(get_current_user)]):
    workouts = session.exec(select(Workout).where(Workout.user_id == current_user.user_id)).all()
    return workouts
    


# Route to add a whole new workout, with the exercise and set
@router.post("/new_workout")
def create_workout(
    workout: WorkoutCreate,
    workout_exercise: WorkoutExercise,
    sets: SetCreate,
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

@router.post("/add_workout_exercise")
def add_workout_exercise(
    workout_exercise: WorkoutExerciseCreate,
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_user)]
):
    workout = session.get(Workout, workout_exercise.workout_id)
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    if workout.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to add exercises to this workout")
    
    new_workout_exercise = WorkoutExercise.model_validate(workout_exercise)
    
    session.add(new_workout_exercise)
    session.commit()
    session.refresh(new_workout_exercise)
    return new_workout_exercise