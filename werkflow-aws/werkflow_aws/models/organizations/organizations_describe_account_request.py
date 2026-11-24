from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDescribeAccountRequest(BaseModel):
    AccountId: StrictStr | None = None
