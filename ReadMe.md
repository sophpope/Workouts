# Fitness Tracker App

#### A full stack fitness application built using Python, Javascript, React, Expo, FastAPI and PostgreSQL

#### This project is currently in development. 

## Project Overview

#### The goal of this project is to create an interactive fitness application, so users can build and record their workouts and track their progress overtime. 

## Current features

* React Frontend running through Expo
* Python & FastAPI Backend
* PostgreSQL Database 
* SQL Models for structuring the data
* API endpoints for retrieving and adding records

## Technologies/Stack

### Frontend

* Javascript
* React 
* Expo

### Backend 

* Python
* FastAPI
* Uvicorn
* SQL Model

### Database

* PostgreSQL

## Installation

1. Clone the repository

2. Create a virtual enviroment in the backend folder

3. Activate the virtual enviroment

4. Install the requirements 
`pip install "fastapi[standard]" sql model`

5. Create a PostgreSQL database for the application 

6. Add details to the config file for connection to the database 

### Currently for backend (to be updated)

7. From inside the backend folder in terminal
`uvicorn main:app --reload`

8. Open the FastAPI documentation from the link in the terminal adding '/docs' at the end or the URL

9. Use the documentation to test the GET & POST requests 

#### Currently for the frontend (to be updated)

10. In the terminal navigate to the main frontend folder 

11. Install npm for JavaScript
`npm install`

12. Start Expo
`npx expo start`

13. Open on the web, mobile app etc. from the selection

## Planned features

* Connect the frontend to the FastAPI endpoints
* Retrieve exercises and user details directly from the PostgreSQL database
* Allow users to create workouts from the frontend and save them to the database
* Edit previous workouts
* View workout history
* Track progress over time