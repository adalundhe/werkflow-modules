from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsUpdateResponsibilityTransferRequest(BaseModel):
    Id: StrictStr
    Name: StrictStr
