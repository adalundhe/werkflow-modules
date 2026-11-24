from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_master import GuardDutyMaster


class GuardDutyGetMasterAccountResponse(BaseModel):
    Master: GuardDutyMaster | None = None
    ResponseMetadata: dict[str, Any] | None = None
