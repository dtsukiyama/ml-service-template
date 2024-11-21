"""Main entry point for the FastAPI application."""

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, HTTPException, status, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints.yourservice import router as your_router
from app.utils.utils import debug_flag, authorize_api_key

app = FastAPI()

config = Config()
logger = setup_service_logging()


@app.on_event("startup")
async def startup_event():
    """Do some startup tasks."""
    pass


def get_cors_origins(config: Config):
    """Get the allowed CORS origins based on the environment."""
    if config.APP_ENV != "prod":
        return [
            "http://app.localhost:3001",
        ]
    else:
        return [
        ]


cors_origins = get_cors_origins(config)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=cors_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    your_router,
    tags=["yourservice"],
    dependencies=[Depends(authorize_api_key)],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """Handle validation errors."""
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    """Handle unhandled exceptions."""
    logger.error(f"Unhandled exception: {type(exc).__name__} occurred. Message: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "code": exc.status_code,
            "name": exc.detail,
            "description": exc.detail,
            "request": str(request.url),
            "method": request.method,
        },
    )


if __name__ == "__main__":
    DEBUG_MODE = debug_flag()
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=DEBUG_MODE)