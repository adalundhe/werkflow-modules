from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_invitation import GuardDutyInvitation


class GuardDutyListInvitationsResponse(BaseModel):
    Invitations: list[GuardDutyInvitation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
