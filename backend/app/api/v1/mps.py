from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.mp import MPRead
from app.repository.mp import get_mps
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[MPRead])
def read_mps(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    """
    Retrieve a list of Members of Parliament with pagination.
    """
    mps = get_mps(db, skip=skip, limit=limit)
    return mps
