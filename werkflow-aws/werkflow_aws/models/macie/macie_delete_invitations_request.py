from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieDeleteInvitationsRequest(BaseModel):
    accountIds: list[StrictStr]
