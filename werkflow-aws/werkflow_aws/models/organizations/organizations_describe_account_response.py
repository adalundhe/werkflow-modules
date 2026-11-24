from __future__ import annotations
from pydantic import BaseModel
from .organizations_account import OrganizationsAccount


class OrganizationsDescribeAccountResponse(BaseModel):
    Account: OrganizationsAccount | None = None
