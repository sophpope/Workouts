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
                                 

class UserCreate(SQLModel):
    username: str
    email: str
    password_hash: str


class ExerciseCreate(SQLModel):
    exercise_name: str
    primary_muscle: str
    secondary_muscle: str
    difficulty: str
    category: str
    equipment: str
    description: str

class PersonalRecordsCreate(SQLModel):
    user_id: int = Field(foreign_key="users.user_id")
    record_type: str
    record_value: int
    achieved_on: date
    exercise_id: int = Field(foreign_key="exercises.exercise_id")
    measurement_type: str
    set_id: int = Field(foreign_key="sets.set_id")

class SetCreate(SQLModel):
    workout_exercise_id: int = Field(foreign_key="workout_exercises.workout_exercise_id")
    set_number: int
    reps: Optional[int]
    weight:Optional[Decimal]
    duration_seconds: Optional[int]
    distance_meters: Optional[Decimal]
    notes: Optional[str]

class WorkoutExerciseCreate(SQLModel):
    workout_id: int = Field(foreign_key="workouts.workout_id")
    exercise_id: int = Field(foreign_key="exercises.exercise_id")
    exercise_order: int

class WorkoutCreate(SQLModel):
    user_id: int = Field(foreign_key="users.user_id")
    workout_name: str
    workout_date: date
    notes: str

# Public models to be used as a response model - showing what our API is returning

class UserPublic(SQLModel):
    username: str

class ExercisePublic(SQLModel):
    exercise_id: int
    exercise_name: str
    primary_muscle: str
    secondary_muscle: str
    difficulty: str
    category: str
    equipment: str
    description: str
    #created_at: datetime

class PersonalRecordsPublic(SQLModel):
    record_type: str
    record_value: int
    achieved_on: date
    measurement_type: str

class SetPublic(SQLModel):
    set_number: int
    reps: int
    weight: Decimal
    duration_seconds: int
    distance_meters: Decimal
    notes: str

class WorkoutExercisePublic(SQLModel):
    workout_exercise_id: int
    workout_id: int 
    exercise_order: int    

class WorkoutPublic(SQLModel):
    workout_name: str
    workout_date: date
    notes: str

# creating new models to create a full workout entry

class newWorkout(SQLModel):
    username: str
    workout_name: str
    workout_date: date
    notes: str

class newWorkoutExercise(SQLModel):
    exercise_id: int
    exercise_order: int

class newSetCreate(SQLModel):
    set_number: int
    reps: Optional[int]
    weight:Optional[Decimal]
    duration_seconds: Optional[int]
    distance_meters: Optional[Decimal]
    notes: Optional[str]
