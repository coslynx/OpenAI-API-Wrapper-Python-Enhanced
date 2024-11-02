from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from openai import OpenAI
from typing import Optional
from utils.logger import logger
from utils.exceptions import OpenAIError, InvalidRequestError
from database.database import get_db

router = APIRouter(prefix="/generate_text")

class GenerateTextRequest(BaseModel):
    prompt: str
    model: str = "text-davinci-003"
    temperature: float = 0.7
    max_tokens: int = 100
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None

@router.post("/")
async def generate_text(request: GenerateTextRequest, openai: OpenAI, db: Optional[Session] = Depends(get_db)):
    """Generates text using OpenAI's API."""

    try:
        response = openai.completions.create(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            top_p=request.top_p,
            frequency_penalty=request.frequency_penalty,
            presence_penalty=request.presence_penalty,
        )

        # Log API call (if database is implemented)
        if db:
            # Implement database logging logic here

        return JSONResponse(
            content={
                "response": response.choices[0].text.strip(),
                "model": response.model,
                "tokens": response.usage.total_tokens,
            }
        )

    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API Error: {e}")
        raise OpenAIError(detail=str(e)) from e
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail="Internal server error") from e