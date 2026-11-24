from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDeclineInvitationsRequest(BaseModel):
    accountIds: list[StrictStr]
