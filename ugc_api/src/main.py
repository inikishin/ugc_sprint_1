import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import events
from core import config
from core.logger import LOGGING
from middleware.auth_middleware import AuthMiddleware


app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(events.router, prefix='/api/v1/events', tags=['events'])

app.add_middleware(AuthMiddleware, auth_url='http://localhost:5000/auth/who')

if __name__ == '__main__':
    # `uvicorn main:app --host 0.0.0.0 --port 8000`
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
