from fastapi import Header, HTTPException

API_KEY = "supersecretkey"

async def verify_api_key(x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPExeception(
            status_code=401,
            detail="Invalid API key"
	)
