from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_account_detail import MacieAccountDetail


class MacieCreateMemberRequest(BaseModel):
    account: MacieAccountDetail
    tags: dict[StrictStr, StrictStr] | None = None
