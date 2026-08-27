from fastapi import FastAPI
from data_processing import df

# To run Swagger 
# Stand in backend/src/backend
# Command: uv run uvicorn api:app

app = FastAPI()

@app.get("/pokemons/stats")
async def show_data():
    return df.to_dict(orient="records")