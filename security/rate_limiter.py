import time
from fastapi import HTTPException

# request history storage
request_log = {}

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

def check_rate_limit(client_id):

    current_time = time.time()

    if client_id not in request_log:
        request_log[client_id] = []

# remove old requests

    request_log[client_id] = [
        t for t in request_log[client_id]
        if current_time - t < WINDOW_SECONDS
    ]

    if len(request_log[client_id]) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    request_log[client_id].append(current_time)
