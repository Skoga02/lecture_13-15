from fastapi import FastAPI
from data_processing import df

app = FastAPI()

@app.get("/pokemons/stats")
async def show_data():
    return df.to_dict(orient="records")