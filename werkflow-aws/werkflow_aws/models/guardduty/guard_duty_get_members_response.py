from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_member import GuardDutyMember
from .guard_duty_unprocessed_account import GuardDutyUnprocessedAccount


class GuardDutyGetMembersResponse(BaseModel):
    Members: list[GuardDutyMember] | None = None
    UnprocessedAccounts: list[GuardDutyUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
