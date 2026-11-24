from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_account import OrganizationsAccount


class OrganizationsListAccountsForParentResponse(BaseModel):
    Accounts: list[OrganizationsAccount] | None = None
    NextToken: StrictStr | None = None
