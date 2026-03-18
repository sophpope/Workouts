from sqlmodel import SQLModel, Field 
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class User(SQLModel, table=True):
    __tablename__="users"
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password_hash: str
    created_at: Optional[datetime] = None


class Exercise(SQLModel, table=True):
    __tablename__="exercises"
    exercise_id: Optional[int] = Field(default=None, primary_key=True)
    exercise_name: str
    primary_muscle: str
    secondary_muscle: str
    difficulty: str
    category: str
    equipment: str
    description: str
    created_at: Optional[datetime] = None

class PersonalRecords(SQLModel, table=True):
    __tablename__="personal_records"
    pr_id: Optional[int]= Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    record_type: str
    record_value: int
    achieved_on: date
    exercise_id: int = Field(foreign_key="exercises.exercise_id")
    measurement_type: str
    set_id: int = Field(foreign_key="sets.set_id")

class Set(SQLModel, table=True):
    __tablename__="sets"
    set_id: Optional[int]= Field(default=None, primary_key=True)
    workout_exercise_id: int = Field(foreign_key="workout_exercises.workout_exercise_id")
    set_number: int
    reps: Optional[int]
    weight:Optional[Decimal]
    duration_seconds: Optional[int]
    distance_meters: Optional[Decimal]
    notes: Optional[str]

class WorkoutExercise(SQLModel, table=True):
    __tablename__="workout_exercises"
    workout_exercise_id: Optional[int]= Field(default=None, primary_key=True)
    workout_id: int = Field(foreign_key="workouts.workout_id")
    exercise_id: int = Field(foreign_key="exercises.exercise_id")
    exercise_order: int

class Workout(SQLModel, table=True):
    __tablename__="workouts"
    workout_id: Optional[int]= Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    workout_name: str
    workout_date: date
    notes: str

# Models for post requests, adding new data to the database                                     
                                     




