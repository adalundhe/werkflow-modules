from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteInvitationsRequest(BaseModel):
    AccountIds: list[StrictStr]
