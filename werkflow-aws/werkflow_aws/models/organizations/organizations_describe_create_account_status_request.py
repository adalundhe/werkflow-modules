from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDescribeCreateAccountStatusRequest(BaseModel):
    CreateAccountRequestId: StrictStr
