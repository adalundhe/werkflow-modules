from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_administrator import GuardDutyAdministrator


class GuardDutyGetAdministratorAccountResponse(BaseModel):
    Administrator: GuardDutyAdministrator | None = None
    ResponseMetadata: dict[str, Any] | None = None
