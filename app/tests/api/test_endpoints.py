import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from fastapi import FastAPI
from unittest.mock import MagicMock, patch
from app.api.endpoints.yourservice import router

# Mock app for testing
app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_health_check():
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}