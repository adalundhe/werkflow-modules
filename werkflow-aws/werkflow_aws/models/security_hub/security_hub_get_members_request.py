from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetMembersRequest(BaseModel):
    AccountIds: list[StrictStr]
