from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_unprocessed_account import GuardDutyUnprocessedAccount


class GuardDutyDeclineInvitationsResponse(BaseModel):
    UnprocessedAccounts: list[GuardDutyUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
