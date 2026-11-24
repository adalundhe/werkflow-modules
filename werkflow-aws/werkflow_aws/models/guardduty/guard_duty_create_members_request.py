from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_account_detail import GuardDutyAccountDetail


class GuardDutyCreateMembersRequest(BaseModel):
    DetectorId: StrictStr
    AccountDetails: list[GuardDutyAccountDetail]
