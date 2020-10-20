from fastapi.testclient import TestClient
from os import getenv
from app.main import app

client = TestClient(app)

