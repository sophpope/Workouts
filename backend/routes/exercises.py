from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from models import Exercise, ExerciseCreate, ExercisePublic
from db_utils import SessionDep, engine

router = APIRouter()


# Returning specific exercise info for crow pose
@router.get("/exercises_specific")
def get_specifc_exercise(session:SessionDep):
    try:
        exercise = select(Exercise).where(Exercise.exercise_name == "L Sit")
        exercises = session.exec(exercise).first()
        return exercises
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Exercise {exercise} not found")

# exercise by id
@router.get("/exercises/{exercise_id}")
def get_exercise_by_id(exercise_id: int, session: SessionDep):
    try:
        exercise = session.exec(select(Exercise).where(Exercise.exercise_id == exercise_id)).first()
        if not exercise:
            raise HTTPException(status_code=404, detail=f"Exercise with ID {exercise_id} not found")
        return exercise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code Error: {str(e)}")
    
@router.get("/exercises")
def get_exercises(session:SessionDep):
    try:
        exercises = session.exec(select(Exercise)).all()
        return exercises
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
#Trying with an exercise that is not in the database, to see if my HTTPException works
@router.get("/exercises_test")
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
@router.post("/create_exercise", response_model=ExercisePublic)
def create_exercise(exercise: ExerciseCreate):
    with Session(engine) as session:
        db_exercise = Exercise.model_validate(exercise)
        session.add(db_exercise)
        session.commit()
        session.refresh(db_exercise)
        return db_exercise