#!/bin/sh

# Start the FastAPI application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload