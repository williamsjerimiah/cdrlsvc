"""Create routes for ddform 1423 drafting"""
from fastapi import status, HTTPException, Response, Depends, APIRouter
from app.schemas.dd1423 import CdrlOut
from app.database.database import db

router = APIRouter(
    prefix="/cdrl/drafting",
    tags=['DD1423']
)

cdrls = db.collection('dd1423')
print(cdrls.all())


@router.get("/", response_model=CdrlOut)
def get_dd1423():
    dd1423 = cdrls.all()
    return dd1423
