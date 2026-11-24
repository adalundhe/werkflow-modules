from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDisassociateFromAdministratorAccountRequest(BaseModel):
    DetectorId: StrictStr
