from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class CdrlBase(BaseModel):
    """Create a schema of the DD Form 1423"""
    contract_line_item_no: str
    exhibit: str
    category: str
    othercat: Optional[str] = None
    system: str
    contract_no: str
    contractor: str
    data_item_number: str
    data_item_title: str
    subtitle: str
    authority: str
    contract_ref: str
    requiring_office: str
    dd250_req: str
    app_code: str
    dist_statement: str
    frequency: str
    first_sub_ate: str
    as_of_date: str
    subsequent_sub_date: str
    distribution: str
    draft: int
    reg: int
    remarks: str


class CdrlOut(CdrlBase):
    """Create a response model to retrieve CDRL details"""
    pass


class CdrlCreate(CdrlBase):
    """Create a schema for use in the DD Form 1423 creation post response"""
    id: str
    created_at: datetime
    created_by: EmailStr
