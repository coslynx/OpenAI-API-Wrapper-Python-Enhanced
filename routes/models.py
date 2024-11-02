from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from openai import OpenAI
from utils.logger import logger
from database.database import get_db

router = APIRouter(prefix="/models")

class ModelsResponse(BaseModel):
    models: List[str]

@router.get("/")
async def get_models(openai: OpenAI, db: Optional[Session] = Depends(get_db)):
    """Retrieves a list of available OpenAI models."""

    try:
        models = openai.models.list()
        model_ids = [model.id for model in models.data]
        return JSONResponse(content={"models": model_ids})
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e
    except Exception as e:
        logger.error(f"Error retrieving models: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e