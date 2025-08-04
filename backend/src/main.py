from fastapi import FastAPI
from typing import Dict, Any

from src.agents.router import router as agents_router
from src.proceedings.router import router as proceedings_router

# Initialize the FastAPI application
app = FastAPI(
    title="Bernardo API",
    description="API for legal proceeding analysis using AI agents",
    version="1.0.0",
)

# Register the routers
app.include_router(agents_router)
app.include_router(proceedings_router)

# Health check endpoint
@app.get("/health", response_model=Dict[str, Any])
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint.
    
    Returns:
        Dict[str, Any]: A dictionary containing the health status of the application.
    """
    return {"status": "healthy", "message": "Application is running successfully"}