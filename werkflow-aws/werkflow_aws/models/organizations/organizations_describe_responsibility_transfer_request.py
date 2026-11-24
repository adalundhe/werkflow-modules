from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDescribeResponsibilityTransferRequest(BaseModel):
    Id: StrictStr
