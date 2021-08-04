from fastapi import APIRouter

from app.routers import *

router = APIRouter()

router.include_router(user_router)
