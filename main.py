from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
import logging
import datetime

# Optional for database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import Database

# Optional for authentication
import jwt
from auth.jwt_handler import create_token, decode_token

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Configure CORS (Optional)
origins = os.getenv("CORS_ORIGINS", "").split(",")
if origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Initialize OpenAI Client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize database (Optional)
if os.getenv("DATABASE_URL"):
    database = Database()

# Authentication Middleware (Optional)
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header:
        token = auth_header.split(" ")[1]
        user_id = decode_token(token)
        if user_id:
            request.state.user_id = user_id
            response = await call_next(request)
            return response
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    else:
        raise HTTPException(status_code=401, detail="Authentication required")

# Define data models for API requests and responses
class GenerateTextRequest(BaseModel):
    prompt: str
    model: str = "text-davinci-003"
    temperature: float = 0.7
    max_tokens: int = 100

class GenerateTextResponse(BaseModel):
    response: str
    model: str
    tokens: int

class ModelsResponse(BaseModel):
    models: list[dict]

class UsageResponse(BaseModel):
    # Define data structure for usage statistics
    pass

# API Endpoints
@app.post("/generate_text")
async def generate_text_route(request: GenerateTextRequest):
    try:
        response = openai.completions.create(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return JSONResponse(
            content={
                "response": response.choices[0].text.strip(),
                "model": response.model,
                "tokens": response.usage.total_tokens,
            }
        )
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/models")
async def models_route():
    try:
        models = openai.models.list()
        return JSONResponse(
            content={"models": [model.id for model in models.data]}
        )
    except Exception as e:
        logging.error(f"Error retrieving models: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/usage")
async def usage_route():
    # Implement logic to retrieve usage data (Optional)
    pass

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)