"""tempate endpoint"""

from fastapi import APIRouter, HTTPException, Request
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from ddtrace import tracer
from app.schemas.yourservice import ExampleSchema

router = APIRouter()


@router.post("/", response_model=None)
async def index(request: ExampleSchema):
    """Fastapi example route."""
    with tracer.trace("exampleservice") as span:
        # Extract and log the request data
        span.set_tag("request", request.json * ())

        try:
            # Call the core business logic

            # Prepare the response with custom headers
            response = {}
            span.set_tag("response", response)

            return JSONResponse(
                content=response,  # Response data
            )

        except Exception as e:
            # Log and raise the error as an HTTPException
            print(f"Error processing request: {str(e)}")
            raise HTTPException(
                status_code=500, detail=f"Error processing your request: {str(e)}"
            )


@router.get("/health")
async def health():
    """Health check route."""
    return {"status": "OK"}