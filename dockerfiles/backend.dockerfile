# Image 
FROM python:3.13-slim 

# everything in backend folder goes into /app folder, wich is created if it dosen't exist before
COPY backend/ /app/

# installs uv 
RUN pip install --no-cache-dir uv

# changes working directory into /app
WORKDIR /app

# installs all dependecies specified in pyproject.toml, without dev packages
RUN uv sync --no-dev

# change working directory to where api.py is located
WORKDIR /app/src/backend

# 0.0.0.0 -> accepts connection from local machine and external
CMD [ "uv" , "run", "uvicorn", "api:app", "--host", "0.0.0.0"]