from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeclineInvitationsRequest(BaseModel):
    AccountIds: list[StrictStr]
