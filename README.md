# llm_learner
learning AI from scratch


commit 1: 

created python fastapi app
 setup commands

python -m venv venv 

/.venv/Scripts/activate.bat

pip install fastapi uvicorn[standard]

pip install pydantic-settings



what was implemented

GET request with path parameter and queries

POST request with basic Pydantic body type

How to import functions/variables from a package - define in init.py

create settings object to dynamically load environment variables and read them - any variable absent raises error

Dependency injetion of the settings object in our functions

different levels of dependency injection - function level, route level, app level

Applied router for grouping routes
