from python:3.9

run pip install fastapi faker jinja2 uvicorn
copy . /ArchExercise
workdir /ArchExercise

cmd ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4961"]