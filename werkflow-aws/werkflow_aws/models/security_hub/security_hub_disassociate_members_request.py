from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDisassociateMembersRequest(BaseModel):
    AccountIds: list[StrictStr]
