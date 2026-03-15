from fastapi import FastAPI, APIRouter


app = FastAPI()
router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello, World!"}

  
@router.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(router)
