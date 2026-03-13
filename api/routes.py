from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from security.auth import verify_api_key
from security.rate_limiter import check_rate_limit
from config.logger import logger

from services.retriever import retrieve
from services.prompt_builder import build_prompt
from services.llm_service import generate
from services.stream_service import stream_response

router = APIRouter()

@router.get("/ask")

async def ask(question: str, api_key=Depends(verify_api_key)):


    logger.info(f"Received question: {question}")

    check_rate_limit(api_key)

    context = await retrieve(question)

    prompt = build_prompt(question, context)

    answer = await generate(prompt)

    logger.info("Response generated")

    return StreamingResponse(stream_response(answer))
