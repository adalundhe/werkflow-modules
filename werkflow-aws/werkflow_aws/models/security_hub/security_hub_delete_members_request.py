from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteMembersRequest(BaseModel):
    AccountIds: list[StrictStr]
