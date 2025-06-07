from fastapi import FastAPI
from app.api.v1.user_routes import router as user_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI app!"}

# Include the user routes
app.include_router(user_router, prefix="/api/v1/users")
