from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_member import GuardDutyMember


class GuardDutyListMembersResponse(BaseModel):
    Members: list[GuardDutyMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
